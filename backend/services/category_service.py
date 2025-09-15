from typing import List

from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from models import Category as CategoryModel
from models import Certification as CertificationModel


class CategoryService:
    def __init__(self):
        pass

    async def get_all_categories(self, db) -> List[CategoryModel]:
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
            print(f"Categories Service Error: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch categories: {str(e)}"
            )

    async def get_category_certifications(
        self,
        db,
        category_slug: str,
        page: int,
        per_page: int
    ):
        """Get paginated certifications for a specific category"""
        try:
            # First, get the category
            category_stmt = select(CategoryModel).where(
                CategoryModel.slug == category_slug
            )
            category_result = await db.execute(category_stmt)
            category = category_result.scalar_one_or_none()

            if not category:
                raise HTTPException(
                    status_code=404,
                    detail="Category not found"
                )

            # Count total certifications
            count_stmt = select(
                func.count(CertificationModel.id)
            ).where(
                CertificationModel.category_id == category.id,
                CertificationModel.is_active
            )
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

            return {
                "certifications": certifications,
                "total": total,
                "page": page,
                "per_page": per_page,
                "has_next": page * per_page < total,
                "has_prev": page > 1,
            }

        except HTTPException:
            raise
        except Exception as e:
            print(f"Category certifications Service Error: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch certifications: {str(e)}"
            )
