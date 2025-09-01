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

class Category(BaseModel):
    id: int
    name: str
    description: str | None
    slug: str
    icon: str | None
    color: str | None

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
    category: Category | None = None

@router.get("/{slug}", response_model=Certification)
async def get_certification(slug: str, db = Depends(get_db)):
    """Get certification by slug with questions and answers"""
    try:
        certification = await db.certification.find_first(
            where={
                "slug": slug,
                "isActive": True
            },
            include={
                "questions": {
                    "include": {"answers": True},
                    "order_by": {"id": "asc"}
                },
                "category": True
            }
        )
        
        if not certification:
            raise HTTPException(status_code=404, detail="Certification not found")
            
        return certification
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch certification")
