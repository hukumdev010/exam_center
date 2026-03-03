from fastapi import Depends

from auth import UserSession
from database import get_db
from .service import ProgressService


class ProgressController:
    def __init__(self):
        self.progress_service = ProgressService()

    async def get_user_progress(
        self,
        current_user: UserSession,
        db=Depends(get_db),
    ):
        """Get user progress for all certifications"""
        return await self.progress_service.get_user_progress(
            db, current_user.user.id
        )

    async def update_user_progress(
        self,
        progress_data: dict,
        current_user: UserSession,
        db=Depends(get_db),
    ):
        """Update user progress for a certification"""
        return await self.progress_service.update_user_progress(
            db, current_user.user.id, progress_data
        )