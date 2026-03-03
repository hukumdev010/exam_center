from datetime import datetime
from uuid import uuid4
from typing import List
from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from fastapi import HTTPException

from models import QuizAttempt as QuizAttemptModel


class QuizAttemptService:
    def __init__(self):
        pass

    async def create_quiz_attempt(
        self,
        db,
        user_id: str,
        attempt_data: dict
    ) -> QuizAttemptModel:
        """Save a completed quiz attempt"""
        try:
            quiz_attempt = QuizAttemptModel(
                id=str(uuid4()),
                user_id=user_id,
                certification_id=attempt_data["certification_id"],
                score=attempt_data["score"],
                total_questions=attempt_data["total_questions"],
                correct_answers=attempt_data["correct_answers"],
                points=attempt_data["points"],
                completed_at=datetime.now(),
            )

            db.add(quiz_attempt)
            await db.commit()
            await db.refresh(quiz_attempt)

            # Auto-create teacher qualification if score is 90% or above
            await self._check_and_create_teacher_qualification(
                db, user_id, quiz_attempt
            )

            # Auto-generate certificate if score is 80% or above
            await self._check_and_create_certificate(
                db, user_id, quiz_attempt
            )

            return quiz_attempt
        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to save quiz attempt")

    async def get_recent_attempts(
        self,
        db,
        user_id: str,
        limit: int = 5
    ) -> List[QuizAttemptModel]:
        """Get recent quiz attempts for a user"""
        try:
            stmt = (
                select(QuizAttemptModel)
                .options(selectinload(QuizAttemptModel.certification))
                .where(QuizAttemptModel.user_id == user_id)
                .order_by(desc(QuizAttemptModel.completed_at))
                .limit(limit)
            )
            result = await db.execute(stmt)
            return result.scalars().all()
        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to fetch recent quiz attempts"
            )

    async def _check_and_create_teacher_qualification(
        self,
        db,
        user_id: str,
        quiz_attempt: QuizAttemptModel
    ) -> None:
        """
        Check if user qualifies to be a teacher and create qualification record
        """
        try:
            # Import here to avoid circular imports
            from modules.teachers.service import TeacherService

            # This will create qualification if score >= 90%
            await TeacherService.create_quiz_qualification(
                db, user_id, quiz_attempt.id
            )
        except Exception:
            # Don't fail the quiz attempt if qualification creation fails
            pass

    async def _check_and_create_certificate(
        self,
        db,
        user_id: str,
        quiz_attempt: QuizAttemptModel
    ) -> None:
        """
        Check if user qualifies for a certificate and create it
        """
        try:
            # Import here to avoid circular imports
            from modules.certificates.service import CertificateService

            certificate_service = CertificateService()

            # This will create certificate if score >= 80%
            await certificate_service.create_certificate(
                db,
                user_id,
                quiz_attempt.id,
                quiz_attempt.certification_id,
                quiz_attempt.score,
                quiz_attempt.total_questions
            )
        except Exception:
            # Don't fail the quiz attempt if certificate creation fails
            pass