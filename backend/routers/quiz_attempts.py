from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from ..database import get_db
from ..auth import get_current_user, UserSession

router = APIRouter()

class QuizAttemptCreate(BaseModel):
    certificationId: int
    score: float
    totalQuestions: int
    correctAnswers: int
    points: int

class QuizAttempt(BaseModel):
    id: int
    userId: str
    certificationId: int
    score: float
    totalQuestions: int
    correctAnswers: int
    points: int
    attemptedAt: datetime

@router.post("/", response_model=QuizAttempt)
async def create_quiz_attempt(
    attempt_data: QuizAttemptCreate,
    current_user: UserSession = Depends(get_current_user),
    db = Depends(get_db)
):
    """Save a completed quiz attempt"""
    try:
        quiz_attempt = await db.quizattempt.create(
            data={
                "userId": current_user.user.id,
                "certificationId": attempt_data.certificationId,
                "score": attempt_data.score,
                "totalQuestions": attempt_data.totalQuestions,
                "correctAnswers": attempt_data.correctAnswers,
                "points": attempt_data.points
            }
        )
        
        return quiz_attempt
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save quiz attempt")
