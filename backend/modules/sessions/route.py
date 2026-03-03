from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from auth import get_current_user, UserSession
from modules.rbac.decorators import require_policies
from .controller import SessionController
from .model import (
    TeachingSession,
    TeachingSessionCreate,
    TeachingSessionUpdate,
    SessionBooking,
    SessionBookingCreate,
    SessionFeedback,
    MyTeachingSession
)
from datetime import datetime

router = APIRouter(tags=["sessions"])


@router.post("/", response_model=TeachingSession,
             dependencies=[Depends(require_policies("createSession"))])
async def create_teaching_session(
    session_data: TeachingSessionCreate,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new teaching session (requires approved teacher profile)
    """
    return await SessionController.create_teaching_session(
        session_data, current_user.user.id, db
    )


@router.put("/{session_id}", response_model=TeachingSession,
            dependencies=[Depends(require_policies("updateSession"))])
async def update_teaching_session(
    session_id: int,
    update_data: TeachingSessionUpdate,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update teaching session (only by session creator)
    """
    return await SessionController.update_teaching_session(
        session_id, update_data, current_user.user.id, db
    )


@router.get("/available", response_model=List[TeachingSession],
            dependencies=[Depends(require_policies("readSession"))])
async def get_available_sessions(
    category_id: Optional[int] = Query(None),
    certification_id: Optional[int] = Query(None),
    session_type: Optional[str] = Query(None),
    min_date: Optional[datetime] = Query(None),
    max_date: Optional[datetime] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: AsyncSession = Depends(get_db)
):
    """
    Get available teaching sessions with filters
    """
    return await SessionController.get_available_sessions(
        category_id, certification_id, session_type,
        min_date, max_date, skip, limit, db
    )


@router.get("/{session_id}", response_model=TeachingSession)
async def get_session_details(
    session_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get session details (public endpoint)
    """
    return await SessionController.get_session_details(session_id, db)


@router.get("/my/teaching", response_model=List[MyTeachingSession])
async def get_my_sessions_as_teacher(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get sessions I'm teaching
    """
    return await SessionController.get_my_sessions_as_teacher(
        current_user.user.id, skip, limit, db
    )


@router.get("/my/bookings", response_model=List[SessionBooking])
async def get_my_bookings_as_student(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get sessions I've booked as a student
    """
    return await SessionController.get_my_bookings_as_student(
        current_user.user.id, skip, limit, db
    )


# Booking endpoints
@router.post("/{session_id}/book", response_model=SessionBooking,
             dependencies=[Depends(require_policies("bookSession"))])
async def book_session(
    session_id: int,
    booking_data: SessionBookingCreate,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Book a teaching session
    """
    return await SessionController.book_session(
        session_id, booking_data, current_user.user.id, db
    )


@router.post("/bookings/{booking_id}/cancel", response_model=SessionBooking)
async def cancel_booking(
    booking_id: int,
    cancellation_reason: Optional[str] = None,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Cancel a session booking
    """
    return await SessionController.cancel_booking(
        booking_id, current_user.user.id, cancellation_reason, db
    )


@router.post("/bookings/{booking_id}/feedback", response_model=SessionBooking)
async def leave_feedback(
    booking_id: int,
    feedback_data: SessionFeedback,
    current_user: UserSession = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Leave feedback for a completed session
    """
    return await SessionController.leave_feedback(
        booking_id, feedback_data, current_user.user.id, db
    )