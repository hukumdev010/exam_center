from fastapi import Depends

from auth import UserSession, get_current_user
from database import get_db
from .service import QuizAttemptService


class QuizAttemptController:
    def __init__(self):
        self.quiz_attempt_service = QuizAttemptService()

    async def create_quiz_attempt(
        self,
        attempt_data: dict,
        current_user: UserSession = Depends(get_current_user),
        db=Depends(get_db),
    ):
        """Save a completed quiz attempt"""
        return await self.quiz_attempt_service.create_quiz_attempt(
            db, current_user.user.id, attempt_data
        )

    async def get_recent_attempts(
        self,
        current_user: UserSession = Depends(get_current_user),
        db=Depends(get_db),
    ):
        """Get recent quiz attempts for the current user"""
        return await self.quiz_attempt_service.get_recent_attempts(
            db, current_user.user.id
        )