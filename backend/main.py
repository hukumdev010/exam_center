from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from .routers import categories, certifications, progress, quiz_attempts, auth
from .database import get_db_client, disconnect_db
from .auth import get_current_user

# Database setup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    db = get_db_client()
    await db.connect()
    yield
    # Shutdown
    await disconnect_db()

app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(certifications.router, prefix="/api/certifications", tags=["certifications"])
app.include_router(progress.router, prefix="/api/progress", tags=["progress"])
app.include_router(quiz_attempts.router, prefix="/api/quiz-attempts", tags=["quiz-attempts"])

@app.get("/")
async def root():
    return {"message": "Exam Center API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
