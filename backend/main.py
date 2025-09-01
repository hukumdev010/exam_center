from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from routers.auth import router as auth_router
from routers.categories import router as categories_router
from routers.certifications import router as certifications_router
from routers.progress import router as progress_router
from routers.quiz_attempts import router as quiz_attempts_router
from database import init_db
from auth import get_current_user

# Database setup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown - SQLAlchemy handles cleanup automatically

app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000", "http://127.0.0.1:3001"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(categories_router, prefix="/api/categories", tags=["categories"])
app.include_router(certifications_router, prefix="/api/certifications", tags=["certifications"])
app.include_router(progress_router, prefix="/api/progress", tags=["progress"])
app.include_router(quiz_attempts_router, prefix="/api/quiz-attempts", tags=["quiz-attempts"])

@app.get("/")
async def root():
    return {"message": "Exam Center API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
