from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from ..database import get_db

router = APIRouter()

class Answer(BaseModel):
    id: int
    text: str
    isCorrect: bool
    questionId: int

class Question(BaseModel):
    id: int
    text: str
    explanation: str | None
    reference: str | None
    certificationId: int
    answers: List[Answer]

class Certification(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None
    passingScore: int
    timeLimit: int | None
    isActive: bool
    categoryId: int
    questions: List[Question] = []

class Category(BaseModel):
    id: int
    name: str
    description: str | None
    slug: str
    icon: str | None
    color: str | None
    certifications: List[Certification] = []

@router.get("/", response_model=List[Category])
async def get_categories(db = Depends(get_db)):
    """Get all categories with their active certifications"""
    try:
        categories = await db.category.find_many(
            include={
                "certifications": {
                    "where": {"isActive": True},
                    "order_by": {"name": "asc"}
                }
            },
            order_by={"name": "asc"}
        )
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch categories")
