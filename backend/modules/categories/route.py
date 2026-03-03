from typing import List

from fastapi import APIRouter, Depends, Query

from database import get_db
from .controller import CategoryController
from .model import Category, PaginatedCertifications, GroupedCategories


router = APIRouter()
category_controller = CategoryController()


@router.get("", response_model=GroupedCategories)
async def get_categories(db=Depends(get_db)):
    """Get all categories grouped by slug without certifications"""
    return await category_controller.get_categories_grouped(db)


@router.get("/with-certifications", response_model=List[Category])
async def get_categories_with_certifications(db=Depends(get_db)):
    """Get all categories with their active certifications (legacy format)"""
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
