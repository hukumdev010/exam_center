from typing import List

from fastapi import APIRouter, Depends, Query

from controllers.category_controller import CategoryController
from database import get_db
from pydantic import BaseModel


router = APIRouter()
category_controller = CategoryController()


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
    return await category_controller.get_categories(db)


@router.get("/{category_slug}/certifications",
            response_model=PaginatedCertifications)
async def get_category_certifications(
    category_slug: str,
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=50, description="Items per page"),
    db=Depends(get_db),
):
    """Get paginated certifications for a specific category"""
    return await category_controller.get_category_certifications(
        category_slug, page, per_page, db
    )
