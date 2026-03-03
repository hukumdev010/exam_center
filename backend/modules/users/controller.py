
from fastapi import HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from auth import get_current_user, UserSession
from .service import UserService
from .model import UserActivity, UserProfile, UserQualifications


class UserController:

    @staticmethod
    async def get_my_profile(
        current_user: UserSession = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ) -> UserProfile:
        """Get current user's profile"""
        user = await UserService.get_user_profile(db, current_user.user.id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return UserProfile.model_validate(user)

    @staticmethod
    async def get_my_activity(
        limit: int = Query(default=10, ge=1, le=100),
        current_user: UserSession = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ) -> UserActivity:
        """Get current user's activity with limit"""
        return await UserService.get_user_activity(
            db, current_user.user.id, limit
        )

    @staticmethod
    async def get_my_qualifications(
        current_user: UserSession,
        db: AsyncSession
    ) -> UserQualifications:
        """Get current user's qualifications (passed certifications)"""
        return await UserService.get_user_qualifications(
            db, current_user.user.id
        )