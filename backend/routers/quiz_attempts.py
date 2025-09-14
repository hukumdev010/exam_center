from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from auth import UserSession, get_current_user
from database import get_db
from models import QuizAttempt as QuizAttemptModel

router = APIRouter()


class QuizAttemptCreate(BaseModel):
    certification_id: int
    score: int
    total_questions: int
    correct_answers: int
    points: int


class QuizAttempt(BaseModel):
    id: str
    user_id: str
    certification_id: int
    score: int
    total_questions: int
    correct_answers: int
    points: int
    completed_at: datetime

    class Config:
        from_attributes = True


@router.post("/", response_model=QuizAttempt)
async def create_quiz_attempt(
    attempt_data: QuizAttemptCreate,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db),
):
    """Save a completed quiz attempt"""
    try:
        quiz_attempt = QuizAttemptModel(
            id=str(uuid4()),
            user_id=current_user.user.id,
            certification_id=attempt_data.certification_id,
            score=attempt_data.score,
            total_questions=attempt_data.total_questions,
            correct_answers=attempt_data.correct_answers,
            points=attempt_data.points,
            completed_at=datetime.now(),
        )

        db.add(quiz_attempt)
        await db.commit()
        await db.refresh(quiz_attempt)

        return quiz_attempt
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to save quiz attempt")
