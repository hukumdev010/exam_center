import google.generativeai as genai
from sqlalchemy import select
from settings.loader import get_settings
from models import QuestionAIAssistant


class AIAssistantService:
    def __init__(self):
        pass

    async def chat_with_ai(self, message: str, context: str = None,
                           current_question: str = None,
                           conversation_history: list = None,
                           question_id: int = None,
                           question_hash: str = None,
                           db=None):
        """Chat with AI assistant for exam help"""
        try:
            # Get settings with API key
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "response": (
                        "I'm sorry, but the AI assistant is currently "
                        "unavailable. Please try again later."
                    ),
                    "error": "Gemini API key not configured",
                }

            # Configure Gemini API with key from settings
            genai.configure(api_key=gemini_api_key)

            # Create the model (using current available model)
            model = genai.GenerativeModel("gemini-2.5-flash")

            # Build conversation context
            system_prompt = (
                "You are an expert AI tutor specializing in certification "
                "exams and technical education. "
                "Your primary goal is to provide comprehensive, detailed "
                "explanations that promote deep understanding.\n\n"
                
                "When answering questions or providing explanations, "
                "ALWAYS include:\n\n"
                
                "1. **Detailed Explanation**: Provide a thorough explanation "
                "of the concept, not just hints. "
                "Break down complex topics into digestible parts and explain "
                "the 'why' behind each answer.\n\n"
                
                "2. **Conceptual Foundation**: Explain the underlying "
                "principles and theory that support the answer. "
                "Connect the current topic to broader concepts in the "
                "field.\n\n"
                
                "3. **Real-World Applications**: Show how this knowledge "
                "applies in practical, real-world scenarios. "
                "Provide examples from industry practice when relevant.\n\n"
                
                "4. **Further Study Resources**: Always suggest specific "
                "topics, keywords, or areas for deeper study. "
                "Recommend what the student should explore next to build "
                "upon this knowledge.\n\n"
                
                "5. **Related Concepts**: Mention related topics and concepts "
                "that connect to the current question. "
                "Help students see the bigger picture and understand how "
                "topics interconnect.\n\n"
                
                "6. **Study Tips**: Provide specific study strategies, "
                "mnemonics, or memory techniques when applicable.\n\n"
                
                "Format your responses clearly with headings and bullet "
                "points for easy reading. "
                "Be encouraging and supportive while maintaining academic "
                "rigor. "
                "If you're unsure about specific details, acknowledge it "
                "and suggest reliable sources for verification."
            )
    
            # Add context if provided
            if context:
                system_prompt += f"\n\nContext: {context}"

            if current_question:
                system_prompt += f"\n\nCurrent Question: {current_question}"

            # Build conversation history
            conversation = f"{system_prompt}\n\nUser: {message}"

            if conversation_history:
                for msg in conversation_history[-5:]:  # Keep last 5 messages
                    role = "User" if msg.get("is_user") else "Assistant"
                    conversation = (
                        f"{role}: {msg.get('content')}\n" +
                        conversation
                    )

            # Check for cached response first if question info is provided
            if question_id and question_hash and db:
                try:
                    # Check if we have a cached response
                    stmt = select(QuestionAIAssistant).where(
                        QuestionAIAssistant.question_id == question_id,
                        QuestionAIAssistant.question_hash == question_hash
                    )
                    result = await db.execute(stmt)
                    cached = result.scalar_one_or_none()
                    
                    if cached:
                        # Update cache hit count
                        cached.cache_hits += 1
                        await db.commit()
                        return {
                            "response": cached.ai_response,
                            "error": None,
                            "cached": True
                        }
                except Exception as e:
                    print(f"Cache check failed: {e}")
                    # Continue with fresh generation
            
            # Configure generation parameters for comprehensive responses
            generation_config = genai.GenerationConfig(
                max_output_tokens=8192,  # Allow longer responses
                temperature=0.7,
                top_p=0.95,
                top_k=40,
            )
            
            # Generate response
            response = model.generate_content(
                conversation,
                generation_config=generation_config
            )
            
            # Save response to database if question info is provided
            if question_id and question_hash and db:
                try:
                    # Save new response to database
                    ai_assistant_record = QuestionAIAssistant(
                        question_id=question_id,
                        question_hash=question_hash,
                        ai_response=response.text,
                        model_name="gemini-2.5-flash",
                        token_count=None,  # Could calculate from response
                        cache_hits=0
                    )
                    db.add(ai_assistant_record)
                    await db.commit()
                    
                    return {
                        "response": response.text,
                        "error": None,
                        "cached": False
                    }
                except Exception as save_error:
                    # Don't fail the response if save fails
                    print(f"Failed to save AI response: {save_error}")
            
            return {"response": response.text, "error": None}

        except Exception as e:
            return {
                "response": (
                    "I'm sorry, I encountered an error. Please try again."
                ),
                "error": str(e)
            }

    async def ai_health(self):
        """Check AI service health"""
        try:
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "status": "unhealthy",
                    "error": "Gemini API key not configured"
                }

            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")
            
            # Configure generation parameters for consistency
            generation_config = genai.GenerationConfig(
                max_output_tokens=1024,  # Shorter for health check
                temperature=0.7,
                top_p=0.95,
                top_k=40,
            )
            
            # Test with a simple prompt
            response = model.generate_content(
                "Hello, are you working?",
                generation_config=generation_config
            )
            
            return {
                "status": "healthy",
                "model": "gemini-2.5-flash",
                "test_response": (
                    response.text[:100] + "..."
                    if len(response.text) > 100
                    else response.text
                )
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }

    async def list_models(self):
        """List available AI models"""
        try:
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "models": [],
                    "error": "Gemini API key not configured"
                }

            genai.configure(api_key=gemini_api_key)
            models = []
            
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    models.append({
                        "name": m.name,
                        "display_name": m.display_name,
                        "description": m.description
                    })

            return {"models": models, "error": None}
        except Exception as e:
            return {
                "models": [],
                "error": str(e)
            }

    async def generate_study_prompt(
        self,
        certification_name: str,
        category: str = None,
        level: str = None,
        user_progress: int = None,
    ):
        """Generate a personalized study prompt"""
        try:
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "prompt": "AI assistant is currently unavailable.",
                    "error": "Gemini API key not configured"
                }

            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")

            # Build the prompt
            prompt_request = (
                f"Generate a personalized study prompt for the "
                f"{certification_name} certification.\n"
            )

            if category:
                prompt_request += f" This is in the {category} category."
            
            if level:
                prompt_request += f" The difficulty level is {level}."
            
            if user_progress:
                prompt_request += (
                    f" The user is {user_progress}% through their preparation."
                )

            prompt_request += """
            
            Please provide:
            1. A motivational opening
            2. Key areas to focus on
            3. Study tips specific to this certification
            4. A suggested daily routine
            
            Keep it encouraging and actionable.
            """

            # Configure generation parameters
            generation_config = genai.GenerationConfig(
                max_output_tokens=4096,  # Medium length for study prompts
                temperature=0.8,  # More creative for motivational content
                top_p=0.95,
                top_k=40,
            )
            
            response = model.generate_content(
                prompt_request,
                generation_config=generation_config
            )
            return {"prompt": response.text, "error": None}

        except Exception as e:
            return {
                "prompt": "Unable to generate study prompt at this time.",
                "error": str(e)
            }