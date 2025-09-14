from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from database import get_db
from models import Answer as AnswerModel
from models import Category as CategoryModel
from models import Certification as CertificationModel
from models import Question as QuestionModel

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


class SimpleCertification(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None
    level: str | None
    duration: int | None
    questions_count: int | None
    is_active: bool
    category_id: int

    class Config:
        from_attributes = True


class Category(BaseModel):
    id: int
    name: str
    description: str | None
    slug: str
    icon: str | None
    color: str | None
    certifications: List[SimpleCertification] = []

    class Config:
        from_attributes = True


class PaginatedCertifications(BaseModel):
    certifications: List[SimpleCertification]
    total: int
    page: int
    per_page: int
    has_next: bool
    has_prev: bool

    class Config:
        from_attributes = True


@router.get("/", response_model=List[Category])
async def get_categories(db=Depends(get_db)):
    """Get all categories with their active certifications"""
    try:
        stmt = (
            select(CategoryModel)
            .options(selectinload(CategoryModel.certifications))
            .order_by(CategoryModel.name)
        )

        result = await db.execute(stmt)
        categories = result.scalars().all()

        # Filter active certifications after loading
        for category in categories:
            category.certifications = [
                cert for cert in category.certifications if cert.is_active
            ]

        return categories
    except Exception as e:
        print(f"Categories API Error: {e}")  # Add logging
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch categories: {str(e)}"
        )


@router.get("/{category_slug}/certifications",
            response_model=PaginatedCertifications)
async def get_category_certifications(
    category_slug: str,
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=50, description="Items per page"),
    db=Depends(get_db),
):
    """Get paginated certifications for a specific category"""
    try:
        # First, get the category
        category_stmt = select(CategoryModel).where(
            CategoryModel.slug == category_slug)
        category_result = await db.execute(category_stmt)
        category = category_result.scalar_one_or_none()

        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        # Count total certifications
        count_stmt = select(
            func.count(
                CertificationModel.id)).where(
            CertificationModel.category_id == category.id,
            CertificationModel.is_active)
        count_result = await db.execute(count_stmt)
        total = count_result.scalar()

        # Get paginated certifications
        offset = (page - 1) * per_page
        stmt = (
            select(CertificationModel)
            .where(
                CertificationModel.category_id == category.id,
                CertificationModel.is_active,
            )
            .order_by(CertificationModel.name)
            .offset(offset)
            .limit(per_page)
        )

        result = await db.execute(stmt)
        certifications = result.scalars().all()

        return PaginatedCertifications(
            certifications=certifications,
            total=total,
            page=page,
            per_page=per_page,
            has_next=page * per_page < total,
            has_prev=page > 1,
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"Category certifications API Error: {e}")
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch certifications: {str(e)}"
        )
