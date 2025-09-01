from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import httpx
import os
from urllib.parse import urlencode

router = APIRouter()

class GoogleAuthURL(BaseModel):
    auth_url: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.get("/google", response_model=GoogleAuthURL)
async def get_google_auth_url():
    """Get Google OAuth2 authorization URL"""
    params = {
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "redirect_uri": f"{os.getenv('API_BASE_URL', 'http://localhost:8000')}/api/auth/google/callback",
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }
    
    auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
    return GoogleAuthURL(auth_url=auth_url)

@router.get("/google/callback")
async def google_callback(code: str = None, error: str = None):
    """Handle Google OAuth2 callback"""
    if error:
        raise HTTPException(status_code=400, detail=f"OAuth error: {error}")
    
    if not code:
        raise HTTPException(status_code=400, detail="Missing authorization code")
    
    # Exchange code for tokens
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": f"{os.getenv('API_BASE_URL', 'http://localhost:8000')}/api/auth/google/callback"
    }
    
    async with httpx.AsyncClient() as client:
        token_response = await client.post(token_url, data=token_data)
        
    if token_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to exchange code for token")
    
    tokens = token_response.json()
    
    # In a real app, you'd validate the ID token and create a session
    # For now, redirect to frontend with the ID token
    frontend_url = f"{os.getenv('FRONTEND_URL', 'http://localhost:3000')}/auth/callback"
    redirect_params = {
        "token": tokens.get("id_token", "")
    }
    
    return RedirectResponse(f"{frontend_url}?{urlencode(redirect_params)}")

@router.post("/logout")
async def logout():
    """Logout user (invalidate token)"""
    # In a real app, you'd invalidate the session/token
    return {"message": "Logged out successfully"}
