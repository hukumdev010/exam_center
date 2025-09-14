import os
import uuid
from urllib.parse import urlencode

import httpx
from fastapi import APIRouter, HTTPException, Query, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from sessions import get_user_session, remove_user_session, set_user_session

router = APIRouter()


class GoogleAuthURL(BaseModel):
    auth_url: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserInfo(BaseModel):
    id: str
    email: str
    name: str
    image: str


@router.get("/me")
async def get_current_user(token: str = Query(...)):
    """Get current user info from session"""
    user_data = get_user_session(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid session token")

    return user_data


@router.post("/logout")
async def logout(token: str = Query(...)):
    """Logout user by removing session"""
    remove_user_session(token)
    return {"message": "Logged out successfully"}


@router.get("/google", response_model=GoogleAuthURL)
async def get_google_auth_url():
    """Get Google OAuth2 authorization URL"""
    params = {
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "redirect_uri": f"{os.getenv('API_BASE_URL', 'http://localhost:8000')}/api/auth/callback/google",
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent",
    }

    auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
    return GoogleAuthURL(auth_url=auth_url)


@router.get("/callback/google")
async def google_callback(code: str = None, error: str = None):
    """Handle Google OAuth2 callback"""
    if error:
        raise HTTPException(status_code=400, detail=f"OAuth error: {error}")

    if not code:
        raise HTTPException(
            status_code=400,
            detail="Missing authorization code")

    try:
        # Exchange code for tokens
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": f"{os.getenv('API_BASE_URL', 'http://127.0.0.1:8000')}/api/auth/callback/google",
        }

        async with httpx.AsyncClient() as client:
            token_response = await client.post(token_url, data=token_data)

        if token_response.status_code != 200:
            raise HTTPException(
                status_code=400, detail="Failed to exchange code for token"
            )

        tokens = token_response.json()
        access_token = tokens.get("access_token")
        id_token = tokens.get("id_token")

        if not access_token:
            raise HTTPException(
                status_code=400,
                detail="No access token received")

        # Get user info from Google
        async with httpx.AsyncClient() as client:
            user_response = await client.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )

        if user_response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to get user info")

        user_info = user_response.json()

        # In a real app, you'd create/update user in database here
        # For now, we'll create a simple JWT token or session

        # Create a simple token (in production, use proper JWT)
        session_token = str(uuid.uuid4())

        # Store user session (in production, use proper session storage)
        user_data = {
            "id": user_info.get("id"),
            "email": user_info.get("email"),
            "name": user_info.get("name"),
            "image": user_info.get("picture"),
        }

        # Store in session
        set_user_session(session_token, user_data)

        # Redirect to frontend with success
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3001")
        redirect_url = f"{frontend_url}/auth/callback?token={session_token}"

        return RedirectResponse(redirect_url)

    except Exception as e:
        # Redirect to frontend with error
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3001")
        error_url = f"{frontend_url}/auth/error?message={str(e)}"
        return RedirectResponse(error_url)


@router.post("/logout")
async def logout():
    """Logout user (invalidate token)"""
    # In a real app, you'd invalidate the session/token
    return {"message": "Logged out successfully"}
