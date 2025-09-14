import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routers.ai_assistant import router as ai_assistant_router
from routers.auth import router as auth_router
from routers.categories import router as categories_router
from routers.certifications import router as certifications_router
from routers.progress import router as progress_router
from routers.quiz_attempts import router as quiz_attempts_router
from settings import get_settings

# Load environment variables
load_dotenv()

print("Environment variables loaded", os.environ.get("GEMINI_API"))

# Database setup


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Initialize settings and database
    settings = await get_settings()
    print(f"Starting application in {settings.environment} mode")
    await init_db()
    yield
    # Shutdown - SQLAlchemy handles cleanup automatically


app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan,
)

# Get settings for CORS configuration


async def get_cors_origins():
    settings = await get_settings()
    default_origins = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
    ]
    if settings.frontend_url not in default_origins:
        default_origins.append(settings.frontend_url)
    return default_origins


# CORS middleware - will be configured properly after startup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Will be updated with proper origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(
    categories_router,
    prefix="/api/categories",
    tags=["categories"])
app.include_router(
    certifications_router,
    prefix="/api/certifications",
    tags=["certifications"])
app.include_router(progress_router, prefix="/api/progress", tags=["progress"])
app.include_router(
    quiz_attempts_router, prefix="/api/quiz-attempts", tags=["quiz-attempts"]
)
app.include_router(
    ai_assistant_router,
    prefix="/api/ai",
    tags=["ai-assistant"])

# Health check endpoints


@app.get("/")
async def root():
    return {"message": "Exam Center API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is operational"}


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


@app.get("/health")
async def health():
    return {"status": "healthy"}
