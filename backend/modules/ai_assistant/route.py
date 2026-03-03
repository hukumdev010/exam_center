from fastapi import APIRouter, Depends

from modules.rbac.decorators import require_policies
from database import get_db
from .controller import AIAssistantController
from .model import (
    ChatRequest, ChatResponse, StudyPromptRequest, StudyPromptResponse
)

router = APIRouter()
ai_controller = AIAssistantController()


@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest, db=Depends(get_db)):
    """Chat with AI assistant for exam help"""
    return await ai_controller.chat_with_ai(request.dict(), db)


@router.get("/health")
async def ai_health():
    """Check AI service health status"""
    return await ai_controller.ai_health()


@router.get("/models")
async def list_models():
    """List available AI models"""
    return await ai_controller.list_models()


@router.post("/study-prompt", response_model=StudyPromptResponse)
async def generate_study_prompt(request: StudyPromptRequest):
    """Generate a personalized study prompt for a certification"""
    return await ai_controller.generate_study_prompt(request.dict())