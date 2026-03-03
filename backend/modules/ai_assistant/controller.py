from .service import AIAssistantService


class AIAssistantController:
    def __init__(self):
        self.ai_service = AIAssistantService()

    async def chat_with_ai(self, request_data: dict, db=None):
        """Chat with AI assistant for exam help"""
        return await self.ai_service.chat_with_ai(
            request_data["message"],
            request_data.get("context"),
            request_data.get("current_question"),
            request_data.get("conversation_history", []),
            request_data.get("question_id"),
            request_data.get("question_hash"),
            db
        )

    async def ai_health(self):
        """Check AI service health"""
        return await self.ai_service.ai_health()

    async def list_models(self):
        """List available AI models"""
        return await self.ai_service.list_models()

    async def generate_study_prompt(self, request_data: dict):
        """Generate a personalized study prompt"""
        return await self.ai_service.generate_study_prompt(
            request_data["certification_name"],
            request_data.get("category"),
            request_data.get("level"),
            request_data.get("user_progress")
        )