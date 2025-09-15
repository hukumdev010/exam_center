from typing import Dict, Any, Optional

from fastapi import HTTPException
from sqlalchemy import or_, select
from sqlalchemy.orm import selectinload

from models import Certification as CertificationModel
from models import Question as QuestionModel
from models import Category as CategoryModel


class CertificationService:
    def __init__(self):
        pass

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

                questions_data.append({
                    "id": question.id,
                    "text": question.text,
                    "explanation": question.explanation,
                    "reference": question.reference,
                    "points": question.points,
                    "certification_id": question.certification_id,
                    "answers": answers_data,
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
