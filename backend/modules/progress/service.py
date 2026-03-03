from datetime import datetime
from typing import List
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models import Certification as CertificationModel
from models import UserProgress as UserProgressModel


class ProgressService:
    def __init__(self):
        pass

    async def get_user_progress(
        self, db, user_id: str
    ) -> List[UserProgressModel]:
        """
        Get user progress for all certifications.
        """
        try:
            stmt = (
                select(UserProgressModel)
                .options(
                    selectinload(UserProgressModel.certification).selectinload(
                        CertificationModel.category
                    )
                )
                .where(UserProgressModel.user_id == user_id)
                .order_by(UserProgressModel.last_active_at.desc())
            )

            result = await db.execute(stmt)
            progress = result.scalars().all()
            return progress
        except Exception:
            raise HTTPException(
                status_code=500, detail="Failed to fetch progress"
            )

    async def update_user_progress(
        self, db, user_id: str, progress_data: dict
    ) -> UserProgressModel:
        """Update user progress for a certification"""
        try:
            # Verify certification exists
            cert_stmt = select(CertificationModel).where(
                CertificationModel.id == progress_data["certification_id"]
            )
            cert_result = await db.execute(cert_stmt)
            certification = cert_result.scalar_one_or_none()

            if not certification:
                raise HTTPException(
                    status_code=404,
                    detail="Certification not found")

            # Check if progress already exists
            progress_stmt = select(UserProgressModel).where(
                UserProgressModel.user_id == user_id,
                UserProgressModel.certification_id == progress_data[
                    "certification_id"
                ],
            )
            progress_result = await db.execute(progress_stmt)
            existing_progress = progress_result.scalar_one_or_none()

            if existing_progress:
                # Update existing progress
                existing_progress.current_question = progress_data[
                    "current_question"
                ]
                existing_progress.correct_answers = progress_data[
                    "correct_answers"
                ]
                existing_progress.points = progress_data["points"]
                existing_progress.is_completed = progress_data["is_completed"]
                existing_progress.last_active_at = datetime.now()
            else:
                # Create new progress
                existing_progress = UserProgressModel(
                    id=str(uuid4()),
                    user_id=user_id,
                    certification_id=progress_data["certification_id"],
                    current_question=progress_data["current_question"],
                    total_questions=certification.questions_count or 0,
                    correct_answers=progress_data["correct_answers"],
                    points=progress_data["points"],
                    is_completed=progress_data["is_completed"],
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
        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to update progress")
