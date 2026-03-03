"""
Central routes configuration for the Exam Center API.
This file imports all module routers and provides a function to
register them with the FastAPI app.
"""

from fastapi import FastAPI

from modules.auth.route import router as auth_router
from modules.categories.route import router as categories_router
from modules.certifications.route import router as certifications_router
from modules.certificates.route import router as certificates_router
from modules.progress.route import router as progress_router
from modules.quiz_attempts.route import router as quiz_attempts_router
from modules.ai_assistant.route import router as ai_assistant_router
from modules.teachers.route import router as teachers_router
from modules.sessions.route import router as sessions_router
from modules.users.route import router as users_router
from modules.rbac.route import router as rbac_router
from modules.syllabus.route import router as syllabus_router
from settings.loader import get_settings


def include_routers(app: FastAPI) -> None:
    """
    Include all module routers in the FastAPI app with their prefixes and tags.
    
    Args:
        app: The FastAPI application instance
    """
    # Authentication routes
    app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
    
    # Categories routes
    app.include_router(
        categories_router,
        prefix="/api/categories",
        tags=["categories"]
    )
    
    # Certifications routes
    app.include_router(
        certifications_router,
        prefix="/api/certifications",
        tags=["certifications"]
    )
    
    # Certificates routes
    app.include_router(
        certificates_router,
        prefix="/api/certificates",
        tags=["certificates"]
    )
    
    # Progress routes
    app.include_router(
        progress_router,
        prefix="/api/progress",
        tags=["progress"]
    )
    
    # Quiz attempts routes
    app.include_router(
        quiz_attempts_router,
        prefix="/api/quiz-attempts",
        tags=["quiz-attempts"]
    )
    
    # AI assistant routes
    app.include_router(
        ai_assistant_router,
        prefix="/api/ai",
        tags=["ai-assistant"]
    )
    
    # Teachers routes
    app.include_router(
        teachers_router,
        prefix="/api/teachers",
        tags=["teachers"]
    )
    
    # Sessions routes
    app.include_router(
        sessions_router,
        prefix="/api/sessions",
        tags=["sessions"]
    )
    
    # Users routes
    app.include_router(
        users_router,
        prefix="/api/users",
        tags=["users"]
    )
    
    # RBAC management routes (admin only)
    app.include_router(
        rbac_router,
        prefix="/api/admin",
        tags=["rbac-management"]
    )
    
    # Syllabus management routes
    app.include_router(
        syllabus_router,
        tags=["syllabus"]
    )

    # Health and system endpoints
    register_system_routes(app)


def register_system_routes(app: FastAPI) -> None:
    """
    Register system-level routes like health checks and configuration.
    
    Args:
        app: The FastAPI application instance
    """
    
    @app.get("/")
    async def root():
        return {"message": "Exam Center API is running"}

    @app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "message": "API is operational and healthy"
        }

    @app.get("/api/config")
    async def get_config():
        """Get non-sensitive configuration information"""
        settings = await get_settings()
        return {
            "environment": settings.environment,
            "debug": settings.debug,
            "api_base_url": settings.api_base_url,
            "frontend_url": settings.frontend_url,
            "aws_region": settings.aws_region,
            "use_secrets_manager": settings._base_settings.use_secrets_manager,
            "secrets_loaded": settings._secrets_cache is not None,
            "database_configured": bool(settings.database_url),
            "google_oauth_configured": bool(
                settings.google_client_id and settings.google_client_secret
            ),
            "gemini_api_configured": bool(settings.gemini_api_key),
        }


# Export individual routers and functions if needed elsewhere
__all__ = [
    "include_routers",
    "register_system_routes",
    "auth_router",
    "categories_router",
    "certifications_router",
    "progress_router",
    "quiz_attempts_router",
    "ai_assistant_router",
    "teachers_router",
    "sessions_router",
    "users_router",
    "rbac_router"
]