from fastapi import APIRouter, Depends
from typing import List

from auth import UserSession, get_current_user
from database import get_db
from modules.rbac.decorators import require_policies
from .controller import QuizAttemptController
from .model import QuizAttemptCreate, QuizAttempt

router = APIRouter()
quiz_attempt_controller = QuizAttemptController()


@router.post("", response_model=QuizAttempt,
             dependencies=[Depends(require_policies("createQuizAttempt"))])
async def create_quiz_attempt(
    attempt_data: QuizAttemptCreate,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db),
):
    """Save a completed quiz attempt"""
    return await quiz_attempt_controller.create_quiz_attempt(
        attempt_data.dict(), current_user, db
    )


@router.get("/recent", response_model=List[QuizAttempt],
            dependencies=[Depends(require_policies("readQuizAttempt"))])
async def get_recent_quiz_attempts(
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db),
):
    """Get recent quiz attempts for the current user"""
    return await quiz_attempt_controller.get_recent_attempts(
        current_user, db
    )