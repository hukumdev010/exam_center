from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from typing import List
from pydantic import BaseModel
from database import get_db
from models import Certification as CertificationModel, Question as QuestionModel, Answer as AnswerModel, Category as CategoryModel

router = APIRouter()

class Answer(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int

    class Config:
        from_attributes = True

class Question(BaseModel):
    id: int
    text: str
    explanation: str | None
    reference: str | None
    certification_id: int
    answers: List[Answer]

    class Config:
        from_attributes = True

class Category(BaseModel):
    id: int
    name: str
    description: str | None
    slug: str
    icon: str | None
    color: str | None

    class Config:
        from_attributes = True

class Certification(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None
    level: str | None
    duration: int | None
    questions_count: int | None
    is_active: bool
    category_id: int
    questions: List[Question] = []
    category: Category | None = None

    class Config:
        from_attributes = True

@router.get("/{slug}", response_model=Certification)
async def get_certification(slug: str, db = Depends(get_db)):
    """Get certification by slug with questions and answers"""
    try:
        stmt = select(CertificationModel).options(
            selectinload(CertificationModel.questions).selectinload(QuestionModel.answers),
            selectinload(CertificationModel.category)
        ).where(
            CertificationModel.slug == slug,
            CertificationModel.is_active == True
        )
        
        result = await db.execute(stmt)
        certification = result.scalar_one_or_none()
        
        if not certification:
            raise HTTPException(status_code=404, detail="Certification not found")
            
        return certification
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch certification")
