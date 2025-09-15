from fastapi import Depends

from database import get_db
from services.category_service import CategoryService


class CategoryController:   
    def __init__(self):
        self.category_service = CategoryService()

    async def get_categories(self, db=Depends(get_db)):
        """Get all categories with their active certifications"""
        return await self.category_service.get_all_categories(db)

    async def get_category_certifications(
        self,
        category_slug: str,
        page: int = 1,
        per_page: int = 10,
        db=Depends(get_db)
    ):
        """Get paginated certifications for a specific category"""
        return await self.category_service.get_category_certifications(
            db, category_slug, page, per_page
        )
    