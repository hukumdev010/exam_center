from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from datetime import datetime
from ..database import get_db
from ..auth import get_current_user, UserSession

router = APIRouter()

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
    category: Category | None = None

class UserProgress(BaseModel):
    id: int
    userId: str
    certificationId: int
    currentQuestion: int
    totalQuestions: int
    correctAnswers: int
    points: int
    isCompleted: bool
    lastActiveAt: datetime
    certification: Certification

class ProgressUpdate(BaseModel):
    certificationId: int
    currentQuestion: int
    correctAnswers: int
    points: int
    isCompleted: bool

@router.get("/", response_model=List[UserProgress])
async def get_user_progress(
    current_user: UserSession = Depends(get_current_user),
    db = Depends(get_db)
):
    """Get user progress for all certifications"""
    try:
        progress = await db.userprogress.find_many(
            where={"userId": current_user.user.id},
            include={
                "certification": {
                    "include": {"category": True}
                }
            },
            order_by={"lastActiveAt": "desc"}
        )
        return progress
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch progress")

@router.post("/", response_model=UserProgress)
async def update_user_progress(
    progress_data: ProgressUpdate,
    current_user: UserSession = Depends(get_current_user),
    db = Depends(get_db)
):
    """Update user progress for a certification"""
    try:
        # Verify certification exists
        certification = await db.certification.find_unique(
            where={"id": progress_data.certificationId},
            include={"questions": True}
        )
        
        if not certification:
            raise HTTPException(status_code=404, detail="Certification not found")
        
        # Upsert progress
        progress = await db.userprogress.upsert(
            where={
                "userId_certificationId": {
                    "userId": current_user.user.id,
                    "certificationId": progress_data.certificationId
                }
            },
            data={
                "update": {
                    "currentQuestion": progress_data.currentQuestion,
                    "correctAnswers": progress_data.correctAnswers,
                    "points": progress_data.points,
                    "isCompleted": progress_data.isCompleted,
                    "lastActiveAt": datetime.now()
                },
                "create": {
                    "userId": current_user.user.id,
                    "certificationId": progress_data.certificationId,
                    "currentQuestion": progress_data.currentQuestion,
                    "totalQuestions": len(certification.questions),
                    "correctAnswers": progress_data.correctAnswers,
                    "points": progress_data.points,
                    "isCompleted": progress_data.isCompleted,
                    "lastActiveAt": datetime.now()
                }
            },
            include={
                "certification": {
                    "include": {"category": True}
                }
            }
        )
        
        return progress
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update progress")
