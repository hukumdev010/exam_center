from contextlib import asynccontextmanager
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routes import include_routers
# Load environment variables initially
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Initialize settings and database
    await init_db()
    yield
    # Shutdown - SQLAlchemy handles cleanup automatically


app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware - allow credentials for cookie-based authentication
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
]

# Add frontend URL from env if specified
frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    allowed_origins.append(frontend_url)

# Allow ngrok URLs in development
ngrok_url = os.getenv("NGROK_URL")
if ngrok_url:
    allowed_origins.append(ngrok_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,  # Enable for cookie-based authentication
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Include routers
include_routers(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
