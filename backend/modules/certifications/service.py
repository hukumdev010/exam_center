from typing import Dict, Any, Optional
import hashlib

from fastapi import HTTPException
from sqlalchemy import or_, select
from sqlalchemy.orm import selectinload

from models import Certification as CertificationModel
from models import Question as QuestionModel
from models import Category as CategoryModel
from models import QuestionAIAssistant


class CertificationService:
    def __init__(self):
        pass
    
    def _generate_question_hash(self, question: QuestionModel) -> str:
        """Generate a hash for a question based on its content"""
        # Include question text and answer texts in the hash
        content = question.text
        for answer in question.answers:
            content += answer.text
        return hashlib.md5(content.encode('utf-8')).hexdigest()

    async def get_certification_by_slug(
        self, db, slug: str
    ) -> Dict[str, Any]:
        """Get certification by slug with questions and answers"""
        try:
            stmt = (
                select(CertificationModel)
                .options(
                    selectinload(CertificationModel.questions)
                    .selectinload(QuestionModel.answers),
                    selectinload(CertificationModel.questions)
                    .selectinload(QuestionModel.ai_assistant),
                    selectinload(CertificationModel.category),
                )
                .where(
                    CertificationModel.slug == slug,
                    CertificationModel.is_active
                )
            )

            result = await db.execute(stmt)
            certification = result.scalar_one_or_none()

            if not certification:
                raise HTTPException(
                    status_code=404,
                    detail="Certification not found"
                )

            # Transform the data to use camelCase for the frontend
            questions_data = []
            for question in certification.questions:
                answers_data = []
                for answer in question.answers:
                    answers_data.append({
                        "id": answer.id,
                        "text": answer.text,
                        # Do not expose isCorrect to avoid showing answers
                        "question_id": answer.question_id,
                    })

                # Check for cached AI assistant response
                ai_assistant_data = None
                question_hash = self._generate_question_hash(question)
                
                # Look for existing AI assistant response with matching hash
                for ai_assistant in question.ai_assistant:
                    if ai_assistant.question_hash == question_hash:
                        ai_assistant_data = {
                            "response": ai_assistant.ai_response,
                            "model_name": ai_assistant.model_name,
                            "cache_hits": ai_assistant.cache_hits,
                            "cached": True,
                            "created_at": (
                                ai_assistant.created_at.isoformat() 
                                if ai_assistant.created_at else None
                            ),
                        }
                        # Increment cache hits
                        ai_assistant.cache_hits += 1
                        # Commit the increment immediately
                        await db.commit()
                        break

                questions_data.append({
                    "id": question.id,
                    "text": question.text,
                    "explanation": question.explanation,
                    "reference": question.reference,
                    "points": question.points,
                    "certification_id": question.certification_id,
                    "answers": answers_data,
                    "ai_assistant": ai_assistant_data,
                    "question_hash": question_hash,  # For frontend caching
                })

            category_data = None
            if certification.category:
                category_data = {
                    "id": certification.category.id,
                    "name": certification.category.name,
                    "description": certification.category.description,
                    "slug": certification.category.slug,
                    "icon": certification.category.icon,
                    "color": certification.category.color,
                }

            return {
                "id": certification.id,
                "name": certification.name,
                "slug": certification.slug,
                "description": certification.description,
                "level": certification.level,
                "duration": certification.duration,
                "questions_count": certification.questions_count,
                "is_active": certification.is_active,
                "category_id": certification.category_id,
                "questions": questions_data,
                "category": category_data,
            }

        except HTTPException:
            raise
        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to fetch certification"
            )

    async def search_certifications(
        self, db, query: Optional[str] = None
    ) -> Dict[str, Any]:
        """Search certifications by query"""
        try:
            stmt = (
                select(CertificationModel)
                .options(selectinload(CertificationModel.category))
                .where(CertificationModel.is_active)
            )

            if query:
                # Search in certification name, description, level and category
                search_filter = or_(
                    CertificationModel.name.ilike(f"%{query}%"),
                    CertificationModel.description.ilike(f"%{query}%"),
                    CertificationModel.level.ilike(f"%{query}%"),
                    CertificationModel.category.has(
                        CategoryModel.name.ilike(f"%{query}%")
                    )
                )
                stmt = stmt.where(search_filter)

            stmt = stmt.order_by(CertificationModel.name)
            result = await db.execute(stmt)
            certifications = result.scalars().all()

            # Format the results to match frontend expectations
            results = []
            for cert in certifications:
                category_data = None
                if cert.category:
                    category_data = {
                        "id": cert.category.id,
                        "name": cert.category.name,
                        "description": cert.category.description,
                        "slug": cert.category.slug,
                        "icon": cert.category.icon,
                        "color": cert.category.color,
                    }

                results.append({
                    "id": cert.id,
                    "name": cert.name,
                    "slug": cert.slug,
                    "description": cert.description,
                    "level": cert.level,
                    "duration": cert.duration,
                    "questions_count": cert.questions_count,
                    "is_active": cert.is_active,
                    "category_id": cert.category_id,
                    "category": category_data,
                })

            return {
                "results": results,
                "total": len(results),
                "query": query or ""
            }

        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to search certifications"
            )

    async def save_ai_assistant_response(
        self, 
        db, 
        question_id: int, 
        question_hash: str,
        ai_response: str,
        model_name: str = "gemini-2.5-flash",
        token_count: Optional[int] = None
    ):
        """Save an AI assistant response for a question"""
        try:
            # Check if response already exists
            existing_stmt = select(QuestionAIAssistant).where(
                QuestionAIAssistant.question_id == question_id,
                QuestionAIAssistant.question_hash == question_hash
            )
            result = await db.execute(existing_stmt)
            existing = result.scalar_one_or_none()
            
            if existing:
                # Update existing response
                existing.ai_response = ai_response
                existing.model_name = model_name
                existing.token_count = token_count
                existing.cache_hits = 0  # Reset cache hits for new response
            else:
                # Create new response
                ai_assistant = QuestionAIAssistant(
                    question_id=question_id,
                    question_hash=question_hash,
                    ai_response=ai_response,
                    model_name=model_name,
                    token_count=token_count,
                    cache_hits=0
                )
                db.add(ai_assistant)
            
            await db.commit()
            return True
            
        except Exception as e:
            await db.rollback()
            print(f"Error saving AI assistant response: {e}")
            return False

    async def get_certification_info(
        self, db, slug: str, user_id: Optional[str] = None
    ):
        """Get certification info for quiz start page"""
        try:
            from models import UserProgress as UserProgressModel
            
            # Get certification with category
            stmt = (
                select(CertificationModel)
                .options(selectinload(CertificationModel.category))
                .where(
                    CertificationModel.slug == slug,
                    CertificationModel.is_active
                )
            )
            result = await db.execute(stmt)
            certification = result.scalar_one_or_none()

            if not certification:
                raise HTTPException(
                    status_code=404,
                    detail="Certification not found"
                )

            # Base certification info
            cert_info = {
                "id": certification.id,
                "name": certification.name,
                "slug": certification.slug,
                "description": certification.description,
                "level": certification.level,
                "duration": certification.duration,
                "questions_count": certification.questions_count,
                "benefits": certification.benefits,
                "advantages": certification.advantages,
                "career_benefits": certification.career_benefits,
                "teaching_eligibility": certification.teaching_eligibility,
                "min_score_for_teaching": certification.min_score_for_teaching,
                "min_score_for_certificate": certification.min_score_for_certificate,
                "has_started": False,
                "current_question": None,
                "progress_percentage": 0.0,
                "user_score": None,
            }

            if certification.category:
                cert_info["category"] = {
                    "id": certification.category.id,
                    "name": certification.category.name,
                    "description": certification.category.description,
                    "slug": certification.category.slug,
                    "icon": certification.category.icon,
                    "color": certification.category.color,
                }

            # If user is logged in, check their progress
            if user_id:
                progress_stmt = select(UserProgressModel).where(
                    UserProgressModel.user_id == user_id,
                    UserProgressModel.certification_id == certification.id,
                )
                progress_result = await db.execute(progress_stmt)
                user_progress = progress_result.scalar_one_or_none()

                if user_progress:
                    cert_info["has_started"] = True
                    cert_info["current_question"] = user_progress.current_question
                    cert_info["progress_percentage"] = (
                        (user_progress.current_question / certification.questions_count * 100)
                        if certification.questions_count > 0 else 0.0
                    )
                    cert_info["user_score"] = user_progress.points

            return cert_info

        except HTTPException:
            raise
        except Exception as e:
            print(f"Error getting certification info: {e}")
            raise HTTPException(
                status_code=500,
                detail="Failed to get certification info"
            )

    async def start_quiz(self, db, slug: str, user_id: str):
        """Start a quiz by creating initial progress record"""
        try:
            from models import UserProgress as UserProgressModel
            from uuid import uuid4

            # Get certification
            cert_stmt = select(CertificationModel).where(
                CertificationModel.slug == slug,
                CertificationModel.is_active
            )
            cert_result = await db.execute(cert_stmt)
            certification = cert_result.scalar_one_or_none()

            if not certification:
                raise HTTPException(
                    status_code=404,
                    detail="Certification not found"
                )

            # Check if user already has progress
            progress_stmt = select(UserProgressModel).where(
                UserProgressModel.user_id == user_id,
                UserProgressModel.certification_id == certification.id,
            )
            progress_result = await db.execute(progress_stmt)
            existing_progress = progress_result.scalar_one_or_none()

            if existing_progress:
                return {
                    "message": "Quiz already started",
                    "current_question": existing_progress.current_question,
                    "redirect_to": f"/quiz/{slug}?q={existing_progress.current_question}"
                }

            # Create new progress record
            user_progress = UserProgressModel(
                id=str(uuid4()),
                user_id=user_id,
                certification_id=certification.id,
                current_question=1,
                total_questions=certification.questions_count or 0,
                correct_answers=0,
                points=0,
                is_completed=False,
            )

            db.add(user_progress)
            await db.commit()

            return {
                "message": "Quiz started successfully",
                "current_question": 1,
                "redirect_to": f"/quiz/{slug}?q=1"
            }

        except HTTPException:
            raise
        except Exception as e:
            await db.rollback()
            print(f"Error starting quiz: {e}")
            raise HTTPException(
                status_code=500,
                detail="Failed to start quiz"
            )

    async def get_certification_syllabus(
        self, db, slug: str, current_user=None
    ):
        """Get certification syllabus - accessible by qualified teachers or students"""
        try:
            import json
            from models import TeacherQualification
            from modules.syllabus.service import SyllabusService
            
            # Get certification with syllabus
            stmt = (
                select(CertificationModel)
                .options(selectinload(CertificationModel.category))
                .where(
                    CertificationModel.slug == slug,
                    CertificationModel.is_active
                )
            )
            result = await db.execute(stmt)
            certification = result.scalar_one_or_none()

            if not certification:
                raise HTTPException(
                    status_code=404,
                    detail="Certification not found"
                )

            # Syllabus should be publicly accessible for course information
            has_access = True  # Public access to syllabus
            is_qualified_teacher = False
            
            if current_user and current_user.user:
                user_id = current_user.user.id
                
                # Check if user is a qualified teacher for this certification
                teacher_qual_stmt = select(TeacherQualification).where(
                    TeacherQualification.user_id == user_id,
                    TeacherQualification.certification_id == certification.id,
                    TeacherQualification.is_active == True
                )
                qual_result = await db.execute(teacher_qual_stmt)
                qualification = qual_result.scalar_one_or_none()
                
                if qualification:
                    is_qualified_teacher = True

            # Try to get structured syllabus from new database tables
            syllabus_service = SyllabusService()
            structured_syllabus = await syllabus_service.get_certification_syllabus_structured(
                db, slug
            )
            
            # Fallback to JSON syllabus if structured syllabus doesn't exist
            syllabus_data = None
            if structured_syllabus and structured_syllabus.get('modules'):
                syllabus_data = structured_syllabus
            elif certification.syllabus:
                try:
                    syllabus_data = json.loads(certification.syllabus)
                    # Enhance JSON syllabus with detailed content
                    syllabus_service = SyllabusService()
                    if 'modules' in syllabus_data:
                        for module in syllabus_data['modules']:
                            if 'topics' in module:
                                for topic in module['topics']:
                                    if (isinstance(topic, dict) and
                                            'title' in topic):
                                        detailed_content = (
                                            syllabus_service
                                            ._load_detailed_content_for_topic(
                                                topic['title']
                                            )
                                        )
                                        if detailed_content:
                                            topic['detailed_content'] = (
                                                detailed_content
                                            )
                except (json.JSONDecodeError, TypeError):
                    syllabus_data = {"error": "Invalid syllabus format"}

            return {
                "certification_id": certification.id,
                "certification_name": certification.name,
                "certification_slug": certification.slug,
                "certification_description": certification.description,
                "certification_level": certification.level,
                "category": {
                    "id": certification.category.id,
                    "name": certification.category.name,
                    "slug": certification.category.slug,
                } if certification.category else None,
                "has_access": has_access,
                "is_qualified_teacher": is_qualified_teacher,
                "syllabus": syllabus_data if has_access else None,
                "syllabus_source": (
                    "structured"
                    if (structured_syllabus and
                        structured_syllabus.get('modules'))
                    else "json"
                    if certification.syllabus
                    else "none"
                ),
                "access_message": (
                    "You have teacher access to this syllabus"
                    if is_qualified_teacher
                    else "Syllabus is publicly accessible"
                )
            }

        except HTTPException:
            raise
        except Exception as e:
            print(f"Error getting certification syllabus: {e}")
            raise HTTPException(
                status_code=500,
                detail="Failed to get certification syllabus"
            )