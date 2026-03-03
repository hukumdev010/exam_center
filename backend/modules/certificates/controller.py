from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth import UserSession, get_current_user
from database import get_db
from .service import CertificateService


class CertificateController:
    def __init__(self):
        self.certificate_service = CertificateService()

    async def create_certificate(
        self,
        quiz_attempt_id: str,
        certification_id: int,
        score: int,
        total_questions: int,
        current_user: UserSession = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ):
        """Create a certificate for a completed quiz"""
        return await self.certificate_service.create_certificate(
            db, 
            current_user.user.id, 
            quiz_attempt_id,
            certification_id,
            score,
            total_questions
        )

    async def get_my_certificates(
        self,
        current_user: UserSession = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ):
        """Get all certificates for the current user"""
        return await self.certificate_service.get_user_certificates(
            db, current_user.user.id
        )

    async def download_certificate(
        self,
        certificate_id: str,
        current_user: UserSession = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ):
        """Download certificate PDF"""
        pdf_content = await self.certificate_service.get_certificate_pdf(
            db, certificate_id, current_user.user.id
        )
        
        if not pdf_content:
            raise HTTPException(
                status_code=404, 
                detail="Certificate not found or PDF unavailable"
            )
        
        return pdf_content