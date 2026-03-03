from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from typing import List

from auth import UserSession, get_current_user
from database import get_db
from modules.rbac.decorators import require_policies
from .controller import CertificateController
from .model import Certificate

router = APIRouter()
certificate_controller = CertificateController()


@router.get("", response_model=List[Certificate])
async def get_my_certificates(
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db)
):
    """Get all certificates for the current user"""
    return await certificate_controller.get_my_certificates(current_user, db)


@router.get("/{certificate_id}/download")
async def download_certificate(
    certificate_id: str,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db)
):
    """Download certificate PDF"""
    pdf_content = await certificate_controller.download_certificate(
        certificate_id, current_user, db
    )
    
    return Response(
        content=pdf_content,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=certificate_{certificate_id}.pdf"
        }
    )


@router.post("/generate")
async def generate_certificate(
    quiz_attempt_id: str,
    certification_id: int,
    score: int,
    total_questions: int,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db)
):
    """Generate a certificate for a completed quiz (internal use)"""
    certificate = await certificate_controller.create_certificate(
        quiz_attempt_id, certification_id, score, total_questions, current_user, db
    )
    
    if not certificate:
        raise HTTPException(
            status_code=400,
            detail="Certificate cannot be generated (score too low or already exists)"
        )
    
    return certificate