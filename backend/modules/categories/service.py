from typing import List

from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from models import Category as CategoryModel
from models import Certification as CertificationModel


class CategoryService:
    def __init__(self):
        pass

    async def get_all_categories(self, db) -> List[CategoryModel]:
        """Get all categories with their active certifications"""
        try:
            stmt = (
                select(CategoryModel)
                .options(selectinload(CategoryModel.certifications))
                .order_by(CategoryModel.name)
            )

            result = await db.execute(stmt)
            categories = result.scalars().all()

            # Filter active certifications after loading
            for category in categories:
                category.certifications = [
                    cert for cert in category.certifications if cert.is_active
                ]

            return categories
        except Exception as e:
            print(f"Categories Service Error: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch categories: {str(e)}"
            )

    async def get_category_certifications(
        self,
        db,
        category_slug: str,
        page: int,
        per_page: int
    ):
        """Get paginated certifications for a specific category"""
        try:
            # First, get the category
            category_stmt = select(CategoryModel).where(
                CategoryModel.slug == category_slug
            )
            category_result = await db.execute(category_stmt)
            category = category_result.scalar_one_or_none()

            if not category:
                raise HTTPException(
                    status_code=404,
                    detail="Category not found"
                )

            # Count total certifications
            count_stmt = select(
                func.count(CertificationModel.id)
            ).where(
                CertificationModel.category_id == category.id,
                CertificationModel.is_active
            )
            count_result = await db.execute(count_stmt)
            total = count_result.scalar()

            # Get paginated certifications
            offset = (page - 1) * per_page
            stmt = (
                select(CertificationModel)
                .where(
                    CertificationModel.category_id == category.id,
                    CertificationModel.is_active,
                )
                .order_by(CertificationModel.name)
                .offset(offset)
                .limit(per_page)
            )

            result = await db.execute(stmt)
            certifications = result.scalars().all()

            return {
                "certifications": certifications,
                "total": total,
                "page": page,
                "per_page": per_page,
                "has_next": page * per_page < total,
                "has_prev": page > 1,
            }

        except HTTPException:
            raise
        except Exception as e:
            print(f"Category certifications Service Error: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch certifications: {str(e)}"
            )

    async def get_categories_grouped(self, db):
        """Get categories grouped by logical domains"""
        try:
            # Get all categories
            stmt = (
                select(CategoryModel)
                .order_by(CategoryModel.name)
            )
            result = await db.execute(stmt)
            all_categories = result.scalars().all()

            # Define logical groupings based on category characteristics
            it_keywords = [
                'aws', 'azure', 'google-cloud', 'gcp', 'devops', 'programming',
                'cybersecurity', 'data-analytics', 
                'data-structures-algorithms',
                'project-management', 'networking', 'database', 'linux',
                'system-design', 'computer-science'
            ]

            language_keywords = [
                'arabic', 'chinese', 'french', 'german', 'italian', 'japanese',
                'korean', 'portuguese', 'russian', 'spanish', 'english'
            ]

            academic_keywords = [
                'accounting', 'art-design', 'biology', 'business-studies',
                'chemistry', 'economics', 'environmental-science', 'geography',
                'history', 'mathematics', 'medical', 'anatomy-physiology',
                'music', 'philosophy', 'physical-education', 'physics',
                'political-science', 'psychology', 'science', 'sociology',
                'statistics'
            ]

            # Create logical parent categories
            it_parent = {
                "id": 9999,
                "name": "IT & Technology",
                "description": "Information Technology and Technical Certs",
                "slug": "it",
                "icon": "computer",
                "color": "blue"
            }

            languages_parent = {
                "id": 9998,
                "name": "Languages",
                "description": "Language proficiency certifications",
                "slug": "languages",
                "icon": "language",
                "color": "rose"
            }

            academic_parent = {
                "id": 9997,
                "name": "Academic",
                "description": "Academic subjects and grade-level certs",
                "slug": "academic",
                "icon": "academic",
                "color": "amber"
            }

            # Group categories
            it_categories = []
            language_categories = []
            academic_categories = []

            for category in all_categories:
                if category.slug in it_keywords:
                    it_categories.append(category)
                elif category.slug in language_keywords:
                    language_categories.append(category)
                elif category.slug in academic_keywords:
                    academic_categories.append(category)
                else:
                    # Default to academic for uncategorized
                    academic_categories.append(category)

            groups = []
            
            if it_categories:
                groups.append({
                    "parent": it_parent,
                    "children": it_categories
                })
                
            if language_categories:
                groups.append({
                    "parent": languages_parent,
                    "children": language_categories
                })
                
            if academic_categories:
                groups.append({
                    "parent": academic_parent,
                    "children": academic_categories
                })

            return {
                "groups": groups
            }

        except Exception as e:
            print(f"Categories Grouped Service Error: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch grouped categories: {str(e)}"
            )