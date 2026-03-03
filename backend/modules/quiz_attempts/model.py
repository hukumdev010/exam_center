from datetime import datetime
from pydantic import BaseModel


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