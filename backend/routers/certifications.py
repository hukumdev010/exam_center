from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from auth import get_optional_user
from controllers.certification_controller import CertificationController
from database import get_db
from models import Certification as CertificationModel
from models import Question as QuestionModel
from models import UserProgress as UserProgressModel

router = APIRouter()
certification_controller = CertificationController()


class AnswerSubmission(BaseModel):
    question_id: int
    answer_id: int


class AnswerVerificationResponse(BaseModel):
    is_correct: bool
    points_earned: int
    total_points: int
    explanation: str | None
    reference: str | None


@router.get("/search")
async def search_certifications(
    q: Optional[str] = Query(None, description="Search query"),
    db=Depends(get_db)
):
    """Search certifications"""
    return await certification_controller.search_certifications(q, db)


@router.get("/{slug}")
async def get_certification(slug: str, db=Depends(get_db)):
    """Get certification by slug with questions and answers"""
    return await certification_controller.get_certification(slug, db)


@router.post("/{slug}/verify-answer")
async def verify_answer(
    slug: str,
    answer_submission: AnswerSubmission,
    current_user=Depends(get_optional_user),
    db=Depends(get_db),
):
    """Verify if the submitted answer is correct and update user points"""
    try:
        # Get the certification
        cert_stmt = select(CertificationModel).where(
            CertificationModel.slug == slug, CertificationModel.is_active
        )
        cert_result = await db.execute(cert_stmt)
        certification = cert_result.scalar_one_or_none()

        if not certification:
            raise HTTPException(
                status_code=404, detail="Certification not found"
            )

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
                    update_data["points"] = (
                        UserProgressModel.points + points_earned
                    )

                if update_data:
                    update_stmt = (
                        update(UserProgressModel)
                        .where(
                            UserProgressModel.user_id == user_id,
                            UserProgressModel.certification_id ==
                            certification.id,
                        )
                        .values(**update_data)
                    )
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
                    updated_progress.points if updated_progress
                    else points_earned
                )

        return AnswerVerificationResponse(
            is_correct=is_correct,
            points_earned=points_earned,
            total_points=total_points,
            explanation=question.explanation,
            reference=question.reference,
        )

    except HTTPException:
        raise
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Failed to verify answer")
