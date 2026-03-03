from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from auth import get_current_user, admin_required, UserSession
from modules.rbac.decorators import require_policies
from .controller import TeacherController
from .model import (
    TeacherProfile,
    TeacherProfileCreate,
    TeacherProfileUpdate,
    AdminApprovalRequest,
    TeacherWithQualifications,
    TeacherQualification,
    TeacherStatusEnum
)

router = APIRouter(tags=["teachers"])


@router.post("/apply", response_model=TeacherProfile,
             dependencies=[Depends(require_policies("createTeacher"))])
async def apply_as_teacher(
    profile_data: TeacherProfileCreate,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Apply to become a teacher (requires 90%+ score qualifications)
    """
    return await TeacherController.apply_as_teacher(
        profile_data, current_user.user.id, db
    )


@router.put("/me", response_model=TeacherProfile)
async def update_my_teacher_profile(
    profile_data: TeacherProfileUpdate,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update current user's teacher profile
    """
    return await TeacherController.update_my_teacher_profile(
        profile_data, current_user.user.id, db
    )


@router.get("/me", response_model=TeacherWithQualifications)
async def get_my_teacher_profile(
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's teacher profile with qualifications
    """
    return await TeacherController.get_my_teacher_profile(
        current_user.user.id, db
    )


@router.get("/me/eligibility")
async def check_teaching_eligibility(
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Check if current user is eligible to become a teacher
    """
    return await TeacherController.check_eligibility(current_user.user.id, db)


@router.get("/me/qualifications", response_model=List[TeacherQualification])
async def get_my_qualifications(
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's teaching qualifications
    """
    return await TeacherController.get_my_qualifications(
        current_user.user.id, db
    )


@router.post("/apply-subject/{certification_id}")
async def apply_to_teach_subject(
    certification_id: int,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Apply to teach a specific subject/certification 
    (requires 90%+ score in that certification)
    """
    return await TeacherController.apply_to_teach_subject(
        certification_id, current_user.user.id, db
    )


@router.post("/process-quiz/{quiz_attempt_id}")
async def process_quiz_for_qualification(
    quiz_attempt_id: str,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Process quiz result to potentially create teaching qualification
    This should be called automatically after quiz completion
    """
    qualification = await TeacherController.process_quiz_result(
        quiz_attempt_id, current_user.user.id, db
    )
    
    if qualification:
        return {
            "message": "Congratulations! You qualified to teach this subject",
            "qualification": qualification
        }
    else:
        return {
            "message": "Score below 90% or already qualified for this subject"
        }


@router.get("", response_model=List[TeacherProfile])
async def list_teachers(
    q: Optional[str] = Query(None, description="Search query"),
    status: Optional[TeacherStatusEnum] = Query(None),
    is_available: Optional[bool] = Query(None),
    category_id: Optional[int] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: AsyncSession = Depends(get_db)
):
    """
    List teachers with filters
    """
    return await TeacherController.list_teachers(
        db, q, status, is_available, category_id, skip, limit
    )


@router.get("/{teacher_id}", response_model=TeacherWithQualifications)
async def get_teacher_profile(
    teacher_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get teacher profile by ID with qualifications (public endpoint)
    """
    return await TeacherController.get_teacher_profile(teacher_id, db)


# Admin endpoints
@router.post("/admin/{teacher_id}/approve", response_model=TeacherProfile,
             dependencies=[Depends(require_policies("approveTeacher"))])
async def admin_approve_teacher(
    teacher_id: int,
    approval_data: AdminApprovalRequest,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db)
):
    """
    Admin approval/rejection of teacher application
    """
    return await TeacherController.admin_approve_teacher(
        teacher_id, approval_data, current_user["id"], db
    )