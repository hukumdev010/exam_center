from typing import Optional, List
from pydantic import BaseModel


class AnswerSubmission(BaseModel):
    question_id: int
    answer_id: int


class AnswerVerificationResponse(BaseModel):
    is_correct: bool
    points_earned: int
    total_points: int
    explanation: Optional[str]
    reference: Optional[str]


class AIAssistantRequest(BaseModel):
    question_id: int
    question_hash: str
    ai_response: str
    model_name: Optional[str] = "gemini-2.5-flash"
    token_count: Optional[int] = None


class Answer(BaseModel):
    id: int
    text: str
    question_id: int
    # is_correct is intentionally not included to avoid exposing answers

    class Config:
        from_attributes = True


class Question(BaseModel):
    id: int
    text: str
    explanation: Optional[str]
    reference: Optional[str]
    points: int
    certification_id: int
    answers: List[Answer]

    class Config:
        from_attributes = True


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
    questions: List[Question] = []
    category: Optional[Category] = None

    class Config:
        from_attributes = True


class CertificationInfo(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str]
    level: Optional[str]
    duration: Optional[int]
    questions_count: Optional[int]
    category: Optional[Category] = None
    
    # Benefits and advantages
    benefits: Optional[str] = None
    advantages: Optional[str] = None
    career_benefits: Optional[str] = None
    teaching_eligibility: bool = False
    min_score_for_teaching: int = 90
    min_score_for_certificate: int = 80
    
    # User progress info (if logged in)
    has_started: bool = False
    current_question: Optional[int] = None
    progress_percentage: float = 0.0
    user_score: Optional[int] = None

    class Config:
        from_attributes = True


class CertificationSearch(BaseModel):
    results: List[Certification]
    total: int
    query: str