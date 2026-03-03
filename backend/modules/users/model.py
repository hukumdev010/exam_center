from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserActivityItem(BaseModel):
    """Single activity item for a user"""
    id: str
    type: str  # "quiz_attempt", "progress_update", etc.
    title: str
    description: Optional[str] = None
    score: Optional[int] = None
    certification_name: Optional[str] = None
    certification_id: Optional[int] = None
    points: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserActivity(BaseModel):
    """User activity response model"""
    activities: List[UserActivityItem]
    total_count: int
    
    class Config:
        from_attributes = True


class UserProfile(BaseModel):
    """User profile model"""
    id: str
    name: Optional[str] = None
    email: str
    email_verified: Optional[datetime] = None
    image: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserQualification(BaseModel):
    """User qualification model"""
    id: str
    certification_name: str
    category_name: str
    score: int
    qualified_at: datetime
    can_teach: bool  # True if score >= 90%
    is_teaching: bool  # True if already applied as teacher for this subject
    
    class Config:
        from_attributes = True


class UserQualifications(BaseModel):
    """User qualifications response model"""
    qualifications: List[UserQualification]
    total_count: int
    
    class Config:
        from_attributes = True