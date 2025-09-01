from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from typing import List
from pydantic import BaseModel
from database import get_db
from models import Category as CategoryModel, Certification as CertificationModel, Question as QuestionModel, Answer as AnswerModel

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

    class Config:
        from_attributes = True

class Category(BaseModel):
    id: int
    name: str
    description: str | None
    slug: str
    icon: str | None
    color: str | None
    certifications: List[Certification] = []

    class Config:
        from_attributes = True

@router.get("/", response_model=List[Category])
async def get_categories(db = Depends(get_db)):
    """Get all categories with their active certifications"""
    try:
        stmt = select(CategoryModel).options(
            selectinload(CategoryModel.certifications).where(CertificationModel.is_active == True)
        ).order_by(CategoryModel.name)
        
        result = await db.execute(stmt)
        categories = result.scalars().all()
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch categories")
