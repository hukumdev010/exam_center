from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from auth import get_current_user, UserSession
from .controller import UserController
from .model import UserActivity, UserProfile, UserQualifications


router = APIRouter(tags=["users"])


@router.get("/me", response_model=UserProfile)
async def get_my_profile(
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user's profile"""
    return await UserController.get_my_profile(current_user, db)


@router.get("/me/activity", response_model=UserActivity)
async def get_my_activity(
    limit: int = Query(default=10, ge=1, le=100,
                       description="Number of activities to return"),
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user's recent activity"""
    return await UserController.get_my_activity(limit, current_user, db)


@router.get("/qualifications", response_model=UserQualifications)
async def get_my_qualifications(
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user's qualifications (passed certifications)"""
    return await UserController.get_my_qualifications(current_user, db)