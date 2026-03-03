from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum


class TeacherStatusEnum(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    SUSPENDED = "suspended"


class SessionTypeEnum(str, Enum):
    ONE_ON_ONE = "one_on_one"
    GROUP = "group"


class TeacherQualificationCreate(BaseModel):
    category_id: int
    certification_id: int
    quiz_attempt_id: str
    score_percentage: float


class TeacherQualification(BaseModel):
    id: int
    user_id: str
    category_id: int
    certification_id: int
    quiz_attempt_id: str
    score_percentage: float
    is_active: bool
    qualified_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class TeacherProfileCreate(BaseModel):
    bio: Optional[str] = None
    qualifications: Optional[str] = None
    experience: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    website_url: Optional[str] = None
    experience_years: Optional[int] = None
    hourly_rate_one_on_one: Optional[float] = None
    hourly_rate_group: Optional[float] = None
    max_group_size: int = 10
    languages_spoken: Optional[str] = None  # JSON string
    timezone: Optional[str] = None


class TeacherProfileUpdate(BaseModel):
    bio: Optional[str] = None
    qualifications: Optional[str] = None
    experience: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    website_url: Optional[str] = None
    experience_years: Optional[int] = None
    hourly_rate_one_on_one: Optional[float] = None
    hourly_rate_group: Optional[float] = None
    max_group_size: Optional[int] = None
    is_available: Optional[bool] = None
    languages_spoken: Optional[str] = None
    timezone: Optional[str] = None


class TeacherProfile(BaseModel):
    id: int
    user_id: str
    bio: Optional[str]
    qualifications: Optional[str]
    experience: Optional[str]
    github_url: Optional[str]
    linkedin_url: Optional[str]
    website_url: Optional[str]
    experience_years: Optional[int]
    hourly_rate_one_on_one: Optional[float]
    hourly_rate_group: Optional[float]
    max_group_size: int
    status: TeacherStatusEnum
    is_available: bool
    languages_spoken: Optional[str]
    timezone: Optional[str]
    approved_by: Optional[str]
    approved_at: Optional[datetime]
    rejection_reason: Optional[str]
    admin_notes: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AdminApprovalRequest(BaseModel):
    status: TeacherStatusEnum
    rejection_reason: Optional[str] = None
    admin_notes: Optional[str] = None


class TeacherWithQualifications(TeacherProfile):
    qualifications: List[TeacherQualification]

    class Config:
        from_attributes = True


class TeacherListItem(BaseModel):
    id: int
    user_id: str
    user_name: Optional[str]
    user_email: str
    bio: Optional[str]
    experience_years: Optional[int]
    hourly_rate_one_on_one: Optional[float]
    hourly_rate_group: Optional[float]
    status: TeacherStatusEnum
    is_available: bool
    created_at: datetime
    qualification_count: int

    class Config:
        from_attributes = True