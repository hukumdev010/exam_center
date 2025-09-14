from datetime import datetime
from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from auth import UserSession, get_current_user
from database import get_db
from models import Category as CategoryModel
from models import Certification as CertificationModel
from models import UserProgress as UserProgressModel

router = APIRouter()


class Category(BaseModel):
    id: int
    name: str
    description: str | None
    slug: str
    icon: str | None
    color: str | None

    class Config:
        from_attributes = True


class Certification(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None
    level: str | None
    duration: int | None
    questions_count: int | None
    is_active: bool
    category_id: int
    category: Category | None = None

    class Config:
        from_attributes = True


class UserProgress(BaseModel):
    id: str
    user_id: str
    certification_id: int
    current_question: int
    total_questions: int
    correct_answers: int
    points: int
    is_completed: bool
    last_active_at: datetime
    certification: Certification

    class Config:
        from_attributes = True


class ProgressUpdate(BaseModel):
    certification_id: int
    current_question: int
    correct_answers: int
    points: int
    is_completed: bool


@router.get("/", response_model=List[UserProgress])
async def get_user_progress(
    current_user: UserSession = Depends(get_current_user), db=Depends(get_db)
):
    """Get user progress for all certifications"""
    try:
        stmt = (
            select(UserProgressModel)
            .options(
                selectinload(UserProgressModel.certification).selectinload(
                    CertificationModel.category
                )
            )
            .where(UserProgressModel.user_id == current_user.user.id)
            .order_by(UserProgressModel.last_active_at.desc())
        )

        result = await db.execute(stmt)
        progress = result.scalars().all()
        return progress
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch progress")


@router.post("/", response_model=UserProgress)
async def update_user_progress(
    progress_data: ProgressUpdate,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db),
):
    """Update user progress for a certification"""
    try:
        # Verify certification exists
        cert_stmt = select(CertificationModel).where(
            CertificationModel.id == progress_data.certification_id
        )
        cert_result = await db.execute(cert_stmt)
        certification = cert_result.scalar_one_or_none()

        if not certification:
            raise HTTPException(
                status_code=404,
                detail="Certification not found")

        # Check if progress already exists
        progress_stmt = select(UserProgressModel).where(
            UserProgressModel.user_id == current_user.user.id,
            UserProgressModel.certification_id == progress_data.certification_id,
        )
        progress_result = await db.execute(progress_stmt)
        existing_progress = progress_result.scalar_one_or_none()

        if existing_progress:
            # Update existing progress
            existing_progress.current_question = progress_data.current_question
            existing_progress.correct_answers = progress_data.correct_answers
            existing_progress.points = progress_data.points
            existing_progress.is_completed = progress_data.is_completed
            existing_progress.last_active_at = datetime.now()
        else:
            # Create new progress
            existing_progress = UserProgressModel(
                id=str(uuid4()),
                user_id=current_user.user.id,
                certification_id=progress_data.certification_id,
                current_question=progress_data.current_question,
                total_questions=certification.questions_count or 0,
                correct_answers=progress_data.correct_answers,
                points=progress_data.points,
                is_completed=progress_data.is_completed,
                last_active_at=datetime.now(),
            )
            db.add(existing_progress)

        await db.commit()
        await db.refresh(existing_progress)

        # Load relationships
        stmt = (
            select(UserProgressModel)
            .options(
                selectinload(UserProgressModel.certification).selectinload(
                    CertificationModel.category
                )
            )
            .where(UserProgressModel.id == existing_progress.id)
        )

        result = await db.execute(stmt)
        progress = result.scalar_one()

        return progress
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to update progress")
