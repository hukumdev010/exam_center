from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import and_, or_, select, update
from sqlalchemy.orm import selectinload

from auth import get_optional_user
from database import get_db
from models import Answer as AnswerModel
from models import Category as CategoryModel
from models import Certification as CertificationModel
from models import Question as QuestionModel
from models import UserProgress as UserProgressModel

router = APIRouter()


@router.get("/{slug}")
async def get_certification(slug: str, db=Depends(get_db)):
    """Get certification by slug with questions and answers"""
    try:
        stmt = (
            select(CertificationModel) .options(
                selectinload(
                    CertificationModel.questions).selectinload(
                    QuestionModel.answers),
                selectinload(
                    CertificationModel.category),
            ) .where(
                CertificationModel.slug == slug,
                CertificationModel.is_active))

        result = await db.execute(stmt)
        certification = result.scalar_one_or_none()

        if not certification:
            raise HTTPException(
                status_code=404,
                detail="Certification not found")

        # Manually transform the data to use camelCase for the frontend
        questions_data = []
        for question in certification.questions:
            answers_data = []
            for answer in question.answers:
                answers_data.append(
                    {
                        "id": answer.id,
                        "text": answer.text,
                        # Do not expose isCorrect to avoid showing answers
                        "question_id": answer.question_id,
                    }
                )

            questions_data.append(
                {
                    "id": question.id,
                    "text": question.text,
                    "explanation": question.explanation,
                    "reference": question.reference,
                    "points": question.points,
                    "certification_id": question.certification_id,
                    "answers": answers_data,
                }
            )

        category_data = None
        if certification.category:
            category_data = {
                "id": certification.category.id,
                "name": certification.category.name,
                "description": certification.category.description,
                "slug": certification.category.slug,
                "icon": certification.category.icon,
                "color": certification.category.color,
            }

        return {
            "id": certification.id,
            "name": certification.name,
            "slug": certification.slug,
            "description": certification.description,
            "level": certification.level,
            "duration": certification.duration,
            "questions_count": certification.questions_count,
            "is_active": certification.is_active,
            "category_id": certification.category_id,
            "questions": questions_data,
            "category": category_data,
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Failed to fetch certification")


@router.get("/search")
async def search_certifications(
    q: str = Query(..., min_length=1, description="Search query"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    level: Optional[str] = Query(None, description="Filter by level"),
    db=Depends(get_db),
):
    """Search certifications by name or description"""
    try:
        # Build the base query
        stmt = (
            select(CertificationModel)
            .options(selectinload(CertificationModel.category))
            .where(CertificationModel.is_active)
        )

        # Add search conditions
        search_conditions = []
        if q:
            search_conditions.append(
                or_(
                    CertificationModel.name.ilike(f"%{q}%"),
                    CertificationModel.description.ilike(f"%{q}%"),
                )
            )

        # Add filter conditions
        if category_id:
            search_conditions.append(
                CertificationModel.category_id == category_id)

        if level:
            search_conditions.append(
                CertificationModel.level.ilike(f"%{level}%"))

        if search_conditions:
            stmt = stmt.where(and_(*search_conditions))

        result = await db.execute(stmt)
        certifications = result.scalars().all()

        # Format response
        results = []
        for cert in certifications:
            category_data = None
            if cert.category:
                category_data = {
                    "id": cert.category.id,
                    "name": cert.category.name,
                    "description": cert.category.description,
                    "slug": cert.category.slug,
                    "icon": cert.category.icon,
                    "color": cert.category.color,
                }

            results.append(
                {
                    "id": cert.id,
                    "name": cert.name,
                    "slug": cert.slug,
                    "description": cert.description,
                    "level": cert.level,
                    "duration": cert.duration,
                    "questions_count": cert.questions_count,
                    "is_active": cert.is_active,
                    "category_id": cert.category_id,
                    "category": category_data,
                }
            )

        return {"results": results, "total": len(results), "query": q}

    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Failed to search certifications")


# Pydantic models for answer verification


class AnswerSubmission(BaseModel):
    question_id: int
    answer_id: int


class AnswerVerificationResponse(BaseModel):
    is_correct: bool
    points_earned: int
    total_points: int
    explanation: Optional[str] = None
    reference: Optional[str] = None


@router.post("/{slug}/verify-answer")
async def verify_answer(
    slug: str,
    answer_submission: AnswerSubmission,
    current_user=Depends(get_optional_user),
    db=Depends(get_db),
):
    """Verify if the submitted answer is correct and update user points if logged in"""
    try:
        # Get the certification
        cert_stmt = select(CertificationModel).where(
            CertificationModel.slug == slug, CertificationModel.is_active
        )
        cert_result = await db.execute(cert_stmt)
        certification = cert_result.scalar_one_or_none()

        if not certification:
            raise HTTPException(
                status_code=404,
                detail="Certification not found")

        # Get the question with answers
        question_stmt = (
            select(QuestionModel)
            .options(selectinload(QuestionModel.answers))
            .where(
                QuestionModel.id == answer_submission.question_id,
                QuestionModel.certification_id == certification.id,
            )
        )
        question_result = await db.execute(question_stmt)
        question = question_result.scalar_one_or_none()

        if not question:
            raise HTTPException(status_code=404, detail="Question not found")

        # Find the submitted answer
        submitted_answer = None
        for answer in question.answers:
            if answer.id == answer_submission.answer_id:
                submitted_answer = answer
                break

        if not submitted_answer:
            raise HTTPException(status_code=404, detail="Answer not found")

        # Check if the answer is correct
        is_correct = submitted_answer.is_correct
        points_earned = question.points if is_correct else 0

        # Update user progress if user is logged in
        total_points = 0
        if current_user:
            user_id = current_user.user.id
            # Get or create user progress
            progress_stmt = select(UserProgressModel).where(
                UserProgressModel.user_id == user_id,
                UserProgressModel.certification_id == certification.id,
            )
            progress_result = await db.execute(progress_stmt)
            user_progress = progress_result.scalar_one_or_none()

            if not user_progress:
                # Create new progress record
                user_progress = UserProgressModel(
                    id=f"{user_id}_{certification.id}",
                    user_id=user_id,
                    certification_id=certification.id,
                    total_questions=certification.questions_count or 0,
                    correct_answers=1 if is_correct else 0,
                    points=points_earned,
                    current_question=1,
                )
                db.add(user_progress)
            else:
                # Update existing progress
                update_data = {}
                if is_correct:
                    update_data["correct_answers"] = (
                        UserProgressModel.correct_answers + 1
                    )
                    update_data["points"] = UserProgressModel.points + \
                        points_earned

                if update_data:
                    update_stmt = (
                        update(UserProgressModel) .where(
                            UserProgressModel.user_id == user_id,
                            UserProgressModel.certification_id == certification.id,
                        ) .values(
                            **update_data))
                    await db.execute(update_stmt)

            await db.commit()

            # Get updated total points
            if user_progress:
                total_points = user_progress.points + (
                    points_earned if not user_progress.id else 0
                )
            else:
                # Re-fetch to get updated points
                progress_result = await db.execute(progress_stmt)
                updated_progress = progress_result.scalar_one_or_none()
                total_points = (
                    updated_progress.points if updated_progress else points_earned)

        return AnswerVerificationResponse(
            is_correct=is_correct,
            points_earned=points_earned,
            total_points=total_points,
            explanation=question.explanation,
            reference=question.reference,
        )

    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Failed to verify answer")
