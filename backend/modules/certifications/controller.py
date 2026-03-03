from typing import Optional

from fastapi import Depends

from database import get_db
from .service import CertificationService


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

    async def save_ai_assistant_response(self, db, ai_request):
        """Save AI assistant response for a question"""
        return await self.certification_service.save_ai_assistant_response(
            db,
            ai_request.question_id,
            ai_request.question_hash,
            ai_request.ai_response,
            ai_request.model_name,
            ai_request.token_count
        )

    async def get_certification_info(
        self, slug: str, user_id: Optional[str] = None, db=Depends(get_db)
    ):
        """Get certification info for quiz start page"""
        return await self.certification_service.get_certification_info(
            db, slug, user_id
        )

    async def start_quiz(self, slug: str, user_id: str, db=Depends(get_db)):
        """Start a quiz by creating initial progress record"""
        return await self.certification_service.start_quiz(
            db, slug, user_id
        )

    async def get_certification_syllabus(
        self, slug: str, current_user=None, db=Depends(get_db)
    ):
        """Get certification syllabus - accessible by qualified teachers or students"""
        return await self.certification_service.get_certification_syllabus(
            db, slug, current_user
        )