from typing import List

from fastapi import APIRouter, Depends

from auth import UserSession, get_current_user
from database import get_db
# from modules.rbac.decorators import require_policies
from .controller import ProgressController
from .model import UserProgress, ProgressUpdate

router = APIRouter()
progress_controller = ProgressController()


@router.get("", response_model=List[UserProgress])
# dependencies=[Depends(require_policies("readProgress"))])
async def get_user_progress(
    current_user: UserSession = Depends(get_current_user), db=Depends(get_db)
):
    """Get user progress for all certifications"""
    return await progress_controller.get_user_progress(current_user, db)


@router.post("", response_model=UserProgress)
#  dependencies=[Depends(require_policies("updateProgress"))])
async def update_user_progress(
    progress_data: ProgressUpdate,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db),
):
    """Update user progress for a certification"""
    return await progress_controller.update_user_progress(
        progress_data.dict(), current_user, db
    )