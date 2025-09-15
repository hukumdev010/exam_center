from typing import Optional

from fastapi import Depends

from database import get_db
from services.certification_service import CertificationService


class CertificationController:
    def __init__(self):
        self.certification_service = CertificationService()

    async def get_certification(self, slug: str, db=Depends(get_db)):
        """Get certification by slug with questions and answers"""
        return await self.certification_service.get_certification_by_slug(
            db, slug
        )

    async def search_certifications(
        self, query: Optional[str] = None, db=Depends(get_db)
    ):
        """Search certifications by query"""
        return await self.certification_service.search_certifications(
            db, query
        )
