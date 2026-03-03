from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    description: Optional[str]
    slug: str
    icon: Optional[str]
    color: Optional[str]

    class Config:
        from_attributes = True


class Certification(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str]
    level: Optional[str]
    duration: Optional[int]
    questions_count: Optional[int]
    is_active: bool
    category_id: int
    category: Optional[Category] = None

    class Config:
        from_attributes = True


class UserProgress(BaseModel):
    id: str
    user_id: str
    certification_id: int
    current_question: int
    total_questions: int
    correct_answers: int
    points: int
    is_completed: bool
    last_active_at: datetime
    updated_at: datetime
    certification: Certification

    class Config:
        from_attributes = True


class ProgressUpdate(BaseModel):
    certification_id: int
    current_question: int
    correct_answers: int
    points: int
    is_completed: bool
