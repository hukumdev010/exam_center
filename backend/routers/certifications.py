from typing import Optional

from fastapi import APIRouter, Depends, Query

from controllers.certification_controller import CertificationController
from database import get_db

router = APIRouter()
certification_controller = CertificationController()


@router.get("/{slug}")
async def get_certification(slug: str, db=Depends(get_db)):
    """Get certification by slug with questions and answers"""
    return await certification_controller.get_certification(slug, db)


@router.get("/search")
async def search_certifications(
    q: Optional[str] = Query(None, description="Search query"),
    db=Depends(get_db)
):
    """Search certifications"""
    return await certification_controller.search_certifications(q, db)
