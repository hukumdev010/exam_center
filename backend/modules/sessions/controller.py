from typing import List, Optional
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from .service import SessionService
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


class SessionController:

    @staticmethod
    async def create_teaching_session(
        session_data: TeachingSessionCreate,
        teacher_user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> TeachingSession:
        """
        Create a new teaching session
        """
        try:
            return await SessionService.create_teaching_session(
                db, teacher_user_id, session_data
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def update_teaching_session(
        session_id: int,
        update_data: TeachingSessionUpdate,
        teacher_user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> TeachingSession:
        """
        Update teaching session
        """
        try:
            session = await SessionService.update_teaching_session(
                db, session_id, teacher_user_id, update_data
            )
            if not session:
                raise HTTPException(
                    status_code=404, 
                    detail="Session not found or not owned by you"
                )
            return session
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def book_session(
        session_id: int,
        booking_data: SessionBookingCreate,
        student_user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> SessionBooking:
        """
        Book a teaching session
        """
        try:
            return await SessionService.book_session(
                db, session_id, student_user_id, booking_data
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def cancel_booking(
        booking_id: int,
        student_user_id: str,
        cancellation_reason: Optional[str],
        db: AsyncSession = Depends(get_db)
    ) -> SessionBooking:
        """
        Cancel a session booking
        """
        try:
            booking = await SessionService.cancel_booking(
                db, booking_id, student_user_id, cancellation_reason
            )
            if not booking:
                raise HTTPException(
                    status_code=404, 
                    detail="Booking not found or not owned by you"
                )
            return booking
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def leave_feedback(
        booking_id: int,
        feedback_data: SessionFeedback,
        student_user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> SessionBooking:
        """
        Leave feedback for a completed session
        """
        booking = await SessionService.leave_feedback(
            db, booking_id, student_user_id, feedback_data
        )
        if not booking:
            raise HTTPException(
                status_code=404, 
                detail="Booking not found or not completed"
            )
        return booking

    @staticmethod
    async def get_available_sessions(
        category_id: Optional[int] = None,
        certification_id: Optional[int] = None,
        session_type: Optional[str] = None,
        min_date: Optional[datetime] = None,
        max_date: Optional[datetime] = None,
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
    ) -> List[TeachingSession]:
        """
        Get available teaching sessions
        """
        return await SessionService.get_available_sessions(
            db, category_id, certification_id, session_type, 
            min_date, max_date, skip, limit
        )

    @staticmethod
    async def get_my_sessions_as_teacher(
        teacher_user_id: str,
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
    ) -> List[MyTeachingSession]:
        """
        Get sessions created by teacher
        """
        sessions = await SessionService.get_my_sessions_as_teacher(
            db, teacher_user_id, skip, limit
        )
        return [MyTeachingSession(**session.__dict__) for session in sessions]

    @staticmethod
    async def get_my_bookings_as_student(
        student_user_id: str,
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
    ) -> List[SessionBooking]:
        """
        Get bookings made by student
        """
        return await SessionService.get_my_bookings_as_student(
            db, student_user_id, skip, limit
        )

    @staticmethod
    async def get_session_details(
        session_id: int,
        db: AsyncSession = Depends(get_db)
    ) -> TeachingSession:
        """
        Get session details
        """
        session = await SessionService.get_session_details(db, session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        return session