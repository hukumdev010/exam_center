from typing import List, Optional

import google.generativeai as genai
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from settings.loader import get_settings

router = APIRouter()


class ChatMessage(BaseModel):
    content: str
    is_user: bool


class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None
    current_question: Optional[str] = None
    conversation_history: Optional[List[ChatMessage]] = []


class ChatResponse(BaseModel):
    response: str
    error: Optional[str] = None


@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    Chat with AI assistant for exam help
    """
    try:
        # Get settings with API key
        settings = await get_settings()
        gemini_api_key = settings.gemini_api_key

        if not gemini_api_key:
            return ChatResponse(
                response=(
                    "I'm sorry, but the AI assistant is currently "
                    "unavailable. Please try again later."
                ),
                error="Gemini API key not configured",
            )

        # Configure Gemini API with key from settings
        genai.configure(api_key=gemini_api_key)

        # Initialize the model with current model name - using the latest
        # stable version
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Build the prompt with context
        system_prompt = (
            "You are a helpful AI study assistant. I'm taking an exam and "
            "need help understanding concepts. Please help me learn and "
            "understand the material without directly giving me the answers "
            "to exam questions.\n\n"
            "Please provide:\n"
            "- Clear explanations of concepts\n"
            "- Study tips and learning strategies\n"
            "- Memory techniques\n"
            "- Related examples\n"
            "- Practice suggestions\n\n"
            "Be conversational, encouraging, and educational in your "
            "responses."
        )

        # Add context information
        context_info = ""
        if request.context:
            context_info += f"\nI'm studying: {request.context}"

        if request.current_question:
            context_info += (
                (
                    f"\nHere's the question I'm working on: "
                    f"{request.current_question}"
                )
            )
            context_info += (
                "\nCan you help me understand the concepts being tested "
                "without giving me the direct answer?"
            )

        # Build conversation history
        conversation = ""
        if request.conversation_history:
            conversation = "\nPrevious conversation:\n"
            # Last 3 messages for context
            for msg in request.conversation_history[-3:]:
                role = "Me" if msg.is_user else "You"
                conversation += f"{role}: {msg.content}\n"

        # Complete prompt - more natural like copy-pasting to Gemini
        full_prompt = (
            f"{system_prompt}"
            f"{context_info}"
            f"{conversation}"
            "\n\nMe: "
            f"{request.message}"
        )

        # Generate response
        response = model.generate_content(full_prompt)

        if response.text:
            return ChatResponse(response=response.text)
        else:
            return ChatResponse(
                response=(
                    "I'm sorry, I couldn't generate a response. "
                    "Please try rephrasing your question."
                ),
                error="No response generated",
            )

    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error processing chat request: {str(e)}"
        )


@router.get("/health")
async def ai_health():
    """
    Check if AI service is available
    """
    settings = await get_settings()
    gemini_api_key = settings.gemini_api_key
    return {
        "status": "healthy",
        "gemini_configured": bool(gemini_api_key),
        "api_key_prefix": (
            gemini_api_key[:10] + "..." if gemini_api_key else None
        ),
    }


@router.get("/models")
async def list_models():
    """
    List available Gemini models
    """
    try:
        settings = await get_settings()
        gemini_api_key = settings.gemini_api_key
        if not gemini_api_key:
            raise HTTPException(
                status_code=500,
                detail="Gemini API key not configured")

        genai.configure(api_key=gemini_api_key)
        models = genai.list_models()
        model_info = []
        for model in models:
            if "generateContent" in model.supported_generation_methods:
                model_info.append(
                    {
                        "name": model.name,
                        "display_name": model.display_name,
                        "description": model.description,
                    }
                )

        return {"available_models": model_info}

    except Exception as e:
        return {"error": str(e), "available_models": []}


@router.post("/generate-study-prompt")
async def generate_study_prompt(
        context: str = None,
        current_question: str = None,
        prompt_type: str = "explain"):
    """
    Generate pre-written prompts for different study needs
    """
    prompts = {
        "explain": (
            "Help me understand the key concepts related to "
            f"{context or 'this topic'} "
            "without giving direct answers to exam questions."
        ),
        "study_tips": (
            "What are the most effective study strategies for "
            f"{context or 'this certification'}? "
            "Give me tips to improve my learning and retention."
        ),
        "practice": (
            (
                "Create practice questions similar to professional "
                "certification exams for "
                f"{context or 'this topic'} "
                "to test my understanding."
            )
        ),
        "memory": (
            "What memory techniques and mnemonics can help me remember "
            "important information about "
            f"{context or 'this subject'}?"
        ),
        "clarify": (
            f"Help me understand what concepts are being tested in this "
            f"question without giving the answer: {current_question}"
            if current_question
            else (
                "Help me clarify complex concepts in "
                f"{context or 'my current study material'}."
            )
        ),
    }

    return {
        "prompt": prompts.get(prompt_type, prompts["explain"]),
        "type": prompt_type,
        "context": context,
    }
