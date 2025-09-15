import os

from fastapi import HTTPException
from fastapi.responses import RedirectResponse

from services.auth_service import AuthService
from sessions import get_user_session, remove_user_session


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    async def get_current_user(self, token: str):
        """Get current user info from session"""
        user_data = get_user_session(token)
        if not user_data:
            raise HTTPException(
                status_code=401,
                detail="Invalid session token"
            )
        return user_data

    async def logout(self, token: str):
        """Logout user by removing session"""
        remove_user_session(token)
        return {"message": "Logged out successfully"}

    async def get_google_auth_url(self):
        """Get Google OAuth2 authorization URL"""
        return self.auth_service.get_google_auth_url()

    async def google_callback(self, code: str = None, error: str = None):
        """Handle Google OAuth2 callback"""
        if error:
            raise HTTPException(
                status_code=400,
                detail=f"OAuth error: {error}"
            )

        if not code:
            raise HTTPException(
                status_code=400,
                detail="Missing authorization code")

        try:
            # Get access token
            access_token = await self.auth_service.exchange_code_for_token(
                code
            )
            
            # Get user info
            user_info = await self.auth_service.get_user_info(access_token)
            
            # Create session
            session_token = await self.auth_service.create_user_session(
                user_info
            )
            
            # Redirect to frontend with success
            frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3001")
            redirect_url = (
                f"{frontend_url}/auth/callback?token={session_token}"
            )
            return RedirectResponse(redirect_url)

        except Exception as e:
            # Redirect to frontend with error
            frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3001")
            error_url = f"{frontend_url}/auth/error?message={str(e)}"
            return RedirectResponse(error_url)

    async def logout_simple(self):
        """Logout user (invalidate token)"""
        # In a real app, you'd invalidate the session/token
        return {"message": "Logged out successfully"}
    
