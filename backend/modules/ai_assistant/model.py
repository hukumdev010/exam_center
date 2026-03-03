from typing import List, Optional
from pydantic import BaseModel


class ChatMessage(BaseModel):
    content: str
    is_user: bool


class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None
    current_question: Optional[str] = None
    conversation_history: Optional[List[ChatMessage]] = []
    question_id: Optional[int] = None
    question_hash: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    error: Optional[str] = None


class StudyPromptRequest(BaseModel):
    certification_name: str
    category: Optional[str] = None
    level: Optional[str] = None
    user_progress: Optional[int] = None


class StudyPromptResponse(BaseModel):
    prompt: str
    error: Optional[str] = None