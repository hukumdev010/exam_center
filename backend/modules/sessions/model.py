from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class SessionTypeEnum(str, Enum):
    ONE_ON_ONE = "one_on_one"
    GROUP = "group"


class SessionStatusEnum(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"


class BookingStatusEnum(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class TeachingSessionCreate(BaseModel):
    category_id: int
    certification_id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    session_type: SessionTypeEnum
    max_participants: int = Field(default=1, ge=1, le=50)
    duration_minutes: int = Field(..., ge=15, le=480)  # 15 min to 8 hours
    price_per_participant: float = Field(..., ge=0.0)
    scheduled_at: datetime
    meeting_link: Optional[str] = None
    meeting_password: Optional[str] = None
    notes: Optional[str] = None


class TeachingSessionUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    duration_minutes: Optional[int] = Field(None, ge=15, le=480)
    price_per_participant: Optional[float] = Field(None, ge=0.0)
    scheduled_at: Optional[datetime] = None
    meeting_link: Optional[str] = None
    meeting_password: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[SessionStatusEnum] = None


class TeachingSession(BaseModel):
    id: int
    teacher_id: int
    category_id: int
    certification_id: Optional[int]
    title: str
    description: Optional[str]
    session_type: SessionTypeEnum
    max_participants: int
    current_participants: int
    duration_minutes: int
    price_per_participant: float
    scheduled_at: datetime
    status: SessionStatusEnum
    meeting_link: Optional[str]
    meeting_password: Optional[str]
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SessionBookingCreate(BaseModel):
    booking_notes: Optional[str] = None


class SessionBookingUpdate(BaseModel):
    booking_notes: Optional[str] = None
    cancellation_reason: Optional[str] = None


class SessionFeedback(BaseModel):
    feedback_rating: int = Field(..., ge=1, le=5)
    feedback_comment: Optional[str] = None


class SessionBooking(BaseModel):
    id: int
    session_id: int
    student_id: str
    status: BookingStatusEnum
    amount_paid: float
    payment_method: Optional[str]
    payment_transaction_id: Optional[str]
    booking_notes: Optional[str]
    attendance_confirmed: bool
    feedback_rating: Optional[int]
    feedback_comment: Optional[str]
    booked_at: datetime
    cancelled_at: Optional[datetime]
    cancellation_reason: Optional[str]

    class Config:
        from_attributes = True


class TeachingSessionWithDetails(TeachingSession):
    teacher_name: Optional[str]
    teacher_email: str
    category_name: str
    certification_name: Optional[str]
    available_spots: int

    class Config:
        from_attributes = True


class SessionBookingWithDetails(SessionBooking):
    session_title: str
    teacher_name: Optional[str]
    scheduled_at: datetime
    duration_minutes: int
    student_name: Optional[str]
    student_email: str

    class Config:
        from_attributes = True


class MyTeachingSession(TeachingSession):
    bookings: List[SessionBooking]

    class Config:
        from_attributes = True


class TeacherSchedule(BaseModel):
    date: str
    sessions: List[TeachingSession]

    class Config:
        from_attributes = True