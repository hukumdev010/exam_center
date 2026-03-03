# Auth utilities for backwards compatibility
# This provides centralized auth functions that other modules expect

from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException, Header

from sessions import get_user_session


class User(BaseModel):
    """User model for session data"""
    id: str
    email: str
    name: Optional[str] = None
    image: Optional[str] = None


class UserSession(BaseModel):
    """User session data structure"""
    user: User
    
    @classmethod
    def from_session_data(cls, session_data: dict) -> "UserSession":
        """Create UserSession from raw session data"""
        return cls(
            user=User(
                id=session_data.get("id", ""),
                email=session_data.get("email", ""),
                name=session_data.get("name"),
                image=session_data.get("image")
            )
        )


async def get_current_user(authorization: str = Header(None)) -> UserSession:
    """
    Get current authenticated user from Bearer token.
    Raises HTTPException if user is not authenticated.
    """
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )
    
    # Extract token from Bearer header
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header format. "
                   "Expected 'Bearer <token>'"
        )
    
    token = authorization.replace("Bearer ", "", 1)
    user_data = get_user_session(token)
    if not user_data:
        raise HTTPException(
            status_code=401,
            detail="Invalid session token"
        )
    
    return UserSession.from_session_data(user_data)


async def get_optional_user(
    authorization: str = Header(None)
) -> Optional[UserSession]:
    """
    Get current user from Bearer token if provided and valid.
    Returns None if no token provided or token is invalid.
    Does not raise exceptions for invalid/missing auth.
    """
    if not authorization:
        return None
    
    if not authorization.startswith("Bearer "):
        return None
    
    try:
        token = authorization.replace("Bearer ", "", 1)
        user_data = get_user_session(token)
        if not user_data:
            return None
        
        return UserSession.from_session_data(user_data)
    except Exception:
        # If anything goes wrong, return None (don't raise)
        return None


async def admin_required(authorization: str = Header(None)) -> dict:
    """
    Get current authenticated user and verify admin privileges.
    Raises HTTPException if user is not authenticated or not an admin.
    Returns user data as dict for backwards compatibility.
    """
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header format. "
                   "Expected 'Bearer <token>'"
        )
    
    token = authorization.replace("Bearer ", "", 1)
    user_data = get_user_session(token)
    
    if not user_data:
        raise HTTPException(
            status_code=401,
            detail="Invalid session token"
        )
    
    # Check if user has admin role - you may need to adjust this logic
    # based on how admin privileges are stored in your system
    is_admin = (user_data.get("is_admin", False) or
                user_data.get("role") == "admin")
    
    if not is_admin:
        raise HTTPException(
            status_code=403,
            detail="Admin privileges required"
        )
    
    return user_data