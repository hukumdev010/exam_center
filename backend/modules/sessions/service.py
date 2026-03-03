from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, and_
from models import (
    TeachingSession,
    SessionBooking,
    TeacherProfile,
    SessionType,
    SessionStatus,
    BookingStatus,
    TeacherStatus
)
from .model import (
    TeachingSessionCreate,
    TeachingSessionUpdate,
    SessionBookingCreate,
    SessionFeedback,
)
from datetime import datetime


class SessionService:

    @staticmethod
    async def create_teaching_session(
        db: AsyncSession,
        teacher_user_id: str,
        session_data: TeachingSessionCreate
    ) -> TeachingSession:
        """
        Create a new teaching session
        """
        # Get teacher profile
        teacher_stmt = select(TeacherProfile).where(
            and_(
                TeacherProfile.user_id == teacher_user_id,
                TeacherProfile.status == TeacherStatus.APPROVED
            )
        )
        teacher_result = await db.execute(teacher_stmt)
        teacher_profile = teacher_result.scalar_one_or_none()

        if not teacher_profile:
            raise ValueError("Teacher profile not found or not approved")

        # Validate scheduled time is in the future
        if session_data.scheduled_at <= datetime.utcnow():
            raise ValueError("Session must be scheduled for a future time")

        # For one-on-one sessions, max_participants should be 1
        max_participants = session_data.max_participants
        if session_data.session_type.value == "one_on_one":
            max_participants = 1

        teaching_session = TeachingSession(
            teacher_id=teacher_profile.id,
            category_id=session_data.category_id,
            certification_id=session_data.certification_id,
            title=session_data.title,
            description=session_data.description,
            session_type=SessionType(session_data.session_type.value),
            max_participants=max_participants,
            current_participants=0,
            duration_minutes=session_data.duration_minutes,
            price_per_participant=session_data.price_per_participant,
            scheduled_at=session_data.scheduled_at,
            status=SessionStatus.SCHEDULED,
            meeting_link=session_data.meeting_link,
            meeting_password=session_data.meeting_password,
            notes=session_data.notes
        )

        db.add(teaching_session)
        await db.commit()
        await db.refresh(teaching_session)

        return teaching_session

    @staticmethod
    async def update_teaching_session(
        db: AsyncSession,
        session_id: int,
        teacher_user_id: str,
        update_data: TeachingSessionUpdate
    ) -> Optional[TeachingSession]:
        """
        Update teaching session (only by teacher who created it)
        """
        # Get session and verify ownership
        session_stmt = select(TeachingSession).join(TeacherProfile).where(
            and_(
                TeachingSession.id == session_id,
                TeacherProfile.user_id == teacher_user_id
            )
        )
        result = await db.execute(session_stmt)
        teaching_session = result.scalar_one_or_none()

        if not teaching_session:
            return None

        # Can't update past sessions
        if teaching_session.scheduled_at <= datetime.utcnow():
            raise ValueError("Cannot update past sessions")

        # Update fields
        for field, value in update_data.model_dump(exclude_unset=True).items():
            if field == "status" and value:
                setattr(teaching_session, field, SessionStatus(value.value))
            else:
                setattr(teaching_session, field, value)

        teaching_session.updated_at = datetime.utcnow()

        await db.commit()
        await db.refresh(teaching_session)

        return teaching_session

    @staticmethod
    async def book_session(
        db: AsyncSession,
        session_id: int,
        student_user_id: str,
        booking_data: SessionBookingCreate
    ) -> SessionBooking:
        """
        Book a teaching session
        """
        # Get session
        session_stmt = select(TeachingSession).where(
            TeachingSession.id == session_id
        )
        result = await db.execute(session_stmt)
        teaching_session = result.scalar_one_or_none()

        if not teaching_session:
            raise ValueError("Session not found")

        if teaching_session.status != SessionStatus.SCHEDULED:
            raise ValueError("Session is not available for booking")

        if teaching_session.scheduled_at <= datetime.utcnow():
            raise ValueError("Cannot book past sessions")

        if (
            teaching_session.current_participants
            >= teaching_session.max_participants
        ):
            raise ValueError("Session is fully booked")

        # Check if student already booked this session
        existing_booking_stmt = select(SessionBooking).where(
            and_(
                SessionBooking.session_id == session_id,
                SessionBooking.student_id == student_user_id,
                SessionBooking.status.in_([
                    BookingStatus.PENDING, 
                    BookingStatus.CONFIRMED
                ])
            )
        )
        existing_result = await db.execute(existing_booking_stmt)
        if existing_result.scalar_one_or_none():
            raise ValueError("Already booked this session")

        # Create booking
        booking = SessionBooking(
            session_id=session_id,
            student_id=student_user_id,
            status=BookingStatus.CONFIRMED,  # Auto-confirm for now
            amount_paid=teaching_session.price_per_participant,
            booking_notes=booking_data.booking_notes,
            attendance_confirmed=False
        )

        db.add(booking)

        # Update session participant count
        teaching_session.current_participants += 1

        await db.commit()
        await db.refresh(booking)

        return booking

    @staticmethod
    async def cancel_booking(
        db: AsyncSession,
        booking_id: int,
        student_user_id: str,
        cancellation_reason: Optional[str] = None
    ) -> Optional[SessionBooking]:
        """
        Cancel a session booking
        """
        booking_stmt = select(SessionBooking).options(
            selectinload(SessionBooking.session)
        ).where(
            and_(
                SessionBooking.id == booking_id,
                SessionBooking.student_id == student_user_id
            )
        )
        result = await db.execute(booking_stmt)
        booking = result.scalar_one_or_none()

        if not booking:
            return None

        if booking.status == BookingStatus.CANCELLED:
            raise ValueError("Booking already cancelled")

        if booking.status == BookingStatus.COMPLETED:
            raise ValueError("Cannot cancel completed booking")

        # Check if session is in the past
        if booking.session.scheduled_at <= datetime.utcnow():
            raise ValueError("Cannot cancel past session")

        # Cancel booking
        booking.status = BookingStatus.CANCELLED
        booking.cancelled_at = datetime.utcnow()
        booking.cancellation_reason = cancellation_reason

        # Update session participant count
        booking.session.current_participants -= 1

        await db.commit()
        await db.refresh(booking)

        return booking

    @staticmethod
    async def leave_feedback(
        db: AsyncSession,
        booking_id: int,
        student_user_id: str,
        feedback_data: SessionFeedback
    ) -> Optional[SessionBooking]:
        """
        Leave feedback for a completed session
        """
        booking_stmt = select(SessionBooking).where(
            and_(
                SessionBooking.id == booking_id,
                SessionBooking.student_id == student_user_id,
                SessionBooking.status == BookingStatus.COMPLETED
            )
        )
        result = await db.execute(booking_stmt)
        booking = result.scalar_one_or_none()

        if not booking:
            return None

        booking.feedback_rating = feedback_data.feedback_rating
        booking.feedback_comment = feedback_data.feedback_comment

        await db.commit()
        await db.refresh(booking)

        return booking

    @staticmethod
    async def get_available_sessions(
        db: AsyncSession,
        category_id: Optional[int] = None,
        certification_id: Optional[int] = None,
        session_type: Optional[str] = None,
        min_date: Optional[datetime] = None,
        max_date: Optional[datetime] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[TeachingSession]:
        """
        Get available teaching sessions
        """
        stmt = select(TeachingSession).options(
            selectinload(TeachingSession.teacher),
            selectinload(TeachingSession.category),
            selectinload(TeachingSession.certification)
        )

        conditions = [
            TeachingSession.status == SessionStatus.SCHEDULED,
            TeachingSession.current_participants
            < TeachingSession.max_participants,
            TeachingSession.scheduled_at > datetime.utcnow()
        ]

        if category_id:
            conditions.append(TeachingSession.category_id == category_id)
        if certification_id:
            conditions.append(
                TeachingSession.certification_id == certification_id
            )
        if session_type:
            conditions.append(
                TeachingSession.session_type == SessionType(session_type)
                )
        if min_date:
            conditions.append(TeachingSession.scheduled_at >= min_date)
        if max_date:
            conditions.append(TeachingSession.scheduled_at <= max_date)

        stmt = (
            stmt.where(and_(*conditions))
            .offset(skip)
            .limit(limit)
            .order_by(TeachingSession.scheduled_at.asc())
        )

        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def get_my_sessions_as_teacher(
        db: AsyncSession,
        teacher_user_id: str,
        skip: int = 0,
        limit: int = 100
    ) -> List[TeachingSession]:
        """
        Get sessions created by teacher
        """
        stmt = select(TeachingSession).join(TeacherProfile).options(
            selectinload(TeachingSession.bookings)
        ).where(
            TeacherProfile.user_id == teacher_user_id
        ).offset(skip).limit(limit).order_by(
            TeachingSession.scheduled_at.desc()
        )

        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def get_my_bookings_as_student(
        db: AsyncSession,
        student_user_id: str,
        skip: int = 0,
        limit: int = 100
    ) -> List[SessionBooking]:
        """
        Get bookings made by student
        """
        stmt = select(SessionBooking).options(
            selectinload(SessionBooking.session),
            selectinload(SessionBooking.session).selectinload(
                TeachingSession.teacher
            )
        ).where(
            SessionBooking.student_id == student_user_id
        ).offset(skip).limit(limit).order_by(
            SessionBooking.booked_at.desc()
        )

        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def get_session_details(
        db: AsyncSession,
        session_id: int
    ) -> Optional[TeachingSession]:
        """
        Get session details with teacher and booking info
        """
        stmt = select(TeachingSession).options(
            selectinload(TeachingSession.teacher),
            selectinload(TeachingSession.category),
            selectinload(TeachingSession.certification),
            selectinload(TeachingSession.bookings)
        ).where(TeachingSession.id == session_id)

        result = await db.execute(stmt)
        return result.scalar_one_or_none()