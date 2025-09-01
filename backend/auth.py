from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from google.auth.transport import requests
from google.oauth2 import id_token
from typing import Optional, Dict, Any
from pydantic import BaseModel
import os
import httpx
from database import get_db

security = HTTPBearer()

class User(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    image: Optional[str] = None

class UserSession(BaseModel):
    user: User

async def verify_google_token(token: str) -> Dict[str, Any]:
    """Verify Google ID token and return user info"""
    try:
        # Verify the token with Google
        idinfo = id_token.verify_oauth2_token(
            token, 
            requests.Request(), 
            os.getenv("GOOGLE_CLIENT_ID")
        )
        
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
            
        return idinfo
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}"
        )

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db = Depends(get_db)
) -> UserSession:
    """Get current authenticated user"""
    try:
        # For development, we'll accept a simple bearer token
        # In production, implement proper JWT verification
        token = credentials.credentials
        
        # Verify with Google (in production)
        # For now, let's implement a simple mock verification
        if token.startswith("google_"):
            # Mock Google token verification
            user_info = await verify_google_token(token.replace("google_", ""))
            user_id = user_info["sub"]
            email = user_info["email"]
            name = user_info.get("name")
            picture = user_info.get("picture")
        else:
            # For development - extract user info from token
            # This is NOT secure and should be replaced with proper auth
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token format"
            )
        
        # Get or create user in database
        user = await db.user.upsert(
            where={"email": email},
            data={
                "update": {
                    "name": name,
                    "image": picture,
                },
                "create": {
                    "email": email,
                    "name": name,
                    "image": picture,
                }
            }
        )
        
        return UserSession(
            user=User(
                id=user.id,
                email=user.email,
                name=user.name,
                image=user.image
            )
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

async def get_optional_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db = Depends(get_db)
) -> Optional[UserSession]:
    """Get current user if authenticated, otherwise None"""
    if not credentials:
        return None
    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None
