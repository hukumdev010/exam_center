from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from typing import List
from database import get_db
from models import Certification as CertificationModel, Question as QuestionModel, Answer as AnswerModel, Category as CategoryModel

router = APIRouter()

@router.get("/{slug}")
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
        
        # Manually transform the data to use camelCase for the frontend
        questions_data = []
        for question in certification.questions:
            answers_data = []
            for answer in question.answers:
                answers_data.append({
                    "id": answer.id,
                    "text": answer.text,
                    "isCorrect": answer.is_correct,
                    "question_id": answer.question_id
                })
            
            questions_data.append({
                "id": question.id,
                "text": question.text,
                "explanation": question.explanation,
                "reference": question.reference,
                "points": question.points,
                "certification_id": question.certification_id,
                "answers": answers_data
            })
        
        category_data = None
        if certification.category:
            category_data = {
                "id": certification.category.id,
                "name": certification.category.name,
                "description": certification.category.description,
                "slug": certification.category.slug,
                "icon": certification.category.icon,
                "color": certification.category.color
            }
        
        return {
            "id": certification.id,
            "name": certification.name,
            "slug": certification.slug,
            "description": certification.description,
            "level": certification.level,
            "duration": certification.duration,
            "questions_count": certification.questions_count,
            "is_active": certification.is_active,
            "category_id": certification.category_id,
            "questions": questions_data,
            "category": category_data
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch certification")
