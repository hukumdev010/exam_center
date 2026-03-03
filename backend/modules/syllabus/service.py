"""Syllabus service for managing curriculum content"""

import json
import os
import importlib.util
from typing import Dict, List, Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

from models import (
    Certification,
    SyllabusModule,
    SyllabusTopic,
    TopicContentSection,
    ModuleLearningObjective
)


class SyllabusService:
    """Service for managing syllabus and curriculum content"""

    async def get_certification_syllabus_structured(
        self,
        db: AsyncSession,
        certification_slug: str
    ) -> Optional[Dict[str, Any]]:
        """Get structured syllabus data from database tables"""
        
        # Get certification with all syllabus data
        stmt = select(Certification).options(
            selectinload(Certification.syllabus_modules).options(
                selectinload(SyllabusModule.topics).options(
                    selectinload(SyllabusTopic.content_sections)
                ),
                selectinload(SyllabusModule.learning_objectives)
            )
        ).where(Certification.slug == certification_slug)
        
        result = await db.execute(stmt)
        certification = result.scalar_one_or_none()
        
        if not certification:
            return None
            
        # Convert to structured format
        syllabus_data = {
            "certification_id": certification.id,
            "certification_name": certification.name,
            "certification_slug": certification.slug,
            "modules": []
        }
        
        for module in certification.syllabus_modules:
            module_data = {
                "id": module.id,
                "moduleNumber": module.module_number,
                "title": module.title,
                "description": module.description,
                "duration": module.duration,
                "topics": [],
                "learningObjectives": [
                    obj.objective for obj in module.learning_objectives
                ]
            }
            
            for topic in module.topics:
                topic_data = {
                    "id": topic.id,
                    "title": topic.title,
                    "description": topic.description,
                    "introduction": topic.introduction,
                    "estimatedDuration": topic.estimated_duration,
                    "videoUrl": topic.video_url,
                    "videoStatus": topic.video_status,
                    "content": {}
                }
                
                # Organize content sections by type
                for section in topic.content_sections:
                    if section.section_type not in topic_data["content"]:
                        topic_data["content"][section.section_type] = []
                    
                    json_sections = [
                        "key_points", "practical_examples", "what_to_teach"
                    ]
                    if section.section_type in json_sections:
                        # Try to parse as JSON array, fallback to string
                        try:
                            content = json.loads(section.content)
                        except (json.JSONDecodeError, TypeError):
                            content = section.content
                    else:
                        content = section.content
                    
                    topic_data["content"][section.section_type] = content
                
                # Add detailed content from database if available
                if topic.detailed_content:
                    try:
                        detailed_json = json.loads(topic.detailed_content)
                        topic_data["detailed_content"] = detailed_json
                    except (json.JSONDecodeError, TypeError):
                        # If JSON parsing fails, try to load from seed files
                        detailed_content = (
                            self._load_detailed_content_for_topic(topic.title)
                        )
                        if detailed_content:
                            topic_data["detailed_content"] = detailed_content
                else:
                    # Try to load detailed content from seed files
                    detailed_content = (
                        self._load_detailed_content_for_topic(topic.title)
                    )
                    if detailed_content:
                        topic_data["detailed_content"] = detailed_content
                
                module_data["topics"].append(topic_data)
            
            syllabus_data["modules"].append(module_data)
        
        return syllabus_data

    async def create_module(
        self,
        db: AsyncSession,
        certification_id: int,
        module_data: Dict[str, Any]
    ) -> SyllabusModule:
        """Create a new syllabus module"""
        
        module = SyllabusModule(
            certification_id=certification_id,
            module_number=module_data["module_number"],
            title=module_data["title"],
            description=module_data.get("description"),
            duration=module_data.get("duration"),
            order_index=module_data["order_index"]
        )
        
        db.add(module)
        await db.flush()  # Get the module ID
        
        # Add learning objectives
        objectives = module_data.get("learning_objectives", [])
        for idx, objective in enumerate(objectives):
            obj = ModuleLearningObjective(
                module_id=module.id,
                objective=objective,
                order_index=idx
            )
            db.add(obj)
        
        return module

    async def create_topic(
        self,
        db: AsyncSession,
        module_id: int,
        topic_data: Dict[str, Any]
    ) -> SyllabusTopic:
        """Create a new syllabus topic with content sections"""
        
        topic = SyllabusTopic(
            module_id=module_id,
            title=topic_data["title"],
            description=topic_data.get("description"),
            introduction=topic_data.get("introduction"),
            order_index=topic_data["order_index"],
            estimated_duration=topic_data.get("estimated_duration"),
            video_status="planned"
        )
        
        db.add(topic)
        await db.flush()  # Get the topic ID
        
        # Add content sections
        content = topic_data.get("content", {})
        section_order = 0
        
        for section_type, section_content in content.items():
            if isinstance(section_content, (list, dict)):
                content_str = json.dumps(section_content)
            else:
                content_str = str(section_content)
            
            section = TopicContentSection(
                topic_id=topic.id,
                section_type=section_type,
                content=content_str,
                order_index=section_order
            )
            db.add(section)
            section_order += 1
        
        return topic

    async def update_topic_video_status(
        self,
        db: AsyncSession,
        topic_id: int,
        video_url: Optional[str] = None,
        video_status: str = "planned"
    ) -> bool:
        """Update video information for a topic"""
        
        stmt = select(SyllabusTopic).where(SyllabusTopic.id == topic_id)
        result = await db.execute(stmt)
        topic = result.scalar_one_or_none()
        
        if not topic:
            return False
        
        if video_url:
            topic.video_url = video_url
        topic.video_status = video_status
        
        await db.commit()
        return True

    async def get_topics_for_video_creation(
        self,
        db: AsyncSession,
        certification_slug: str,
        status: str = "planned"
    ) -> List[Dict[str, Any]]:
        """Get topics that need video creation"""
        
        stmt = select(SyllabusTopic).join(
            SyllabusModule
        ).join(
            Certification
        ).options(
            selectinload(SyllabusTopic.content_sections),
            selectinload(SyllabusTopic.module)
        ).where(
            and_(
                Certification.slug == certification_slug,
                SyllabusTopic.video_status == status,
                SyllabusTopic.is_active.is_(True)
            )
        ).order_by(
            SyllabusModule.order_index,
            SyllabusTopic.order_index
        )
        
        result = await db.execute(stmt)
        topics = result.scalars().all()
        
        topics_data = []
        for topic in topics:
            topic_data = {
                "id": topic.id,
                "title": topic.title,
                "module_title": topic.module.title,
                "module_number": topic.module.module_number,
                "description": topic.description,
                "introduction": topic.introduction,
                "content_sections": {}
            }
            
            # Organize content for video creation
            for section in topic.content_sections:
                try:
                    json_sections = [
                        "key_points", "practical_examples", "what_to_teach"
                    ]
                    if section.section_type in json_sections:
                        content = json.loads(section.content)
                    else:
                        content = section.content
                except (json.JSONDecodeError, TypeError):
                    content = section.content
                
                topic_data["content_sections"][section.section_type] = content
            
            topics_data.append(topic_data)
        
        return topics_data

    async def get_topic_detailed_content(
        self,
        db: AsyncSession,
        topic_id: int
    ) -> Optional[Dict[str, Any]]:
        """Get detailed content for a specific topic from both database and seed data"""
        
        # Get topic from database
        stmt = select(SyllabusTopic).options(
            selectinload(SyllabusTopic.content_sections),
            selectinload(SyllabusTopic.module).options(
                selectinload(SyllabusModule.certification)
            )
        ).where(SyllabusTopic.id == topic_id)
        
        result = await db.execute(stmt)
        topic = result.scalar_one_or_none()
        
        if not topic:
            return None
        
        # Base topic information from database
        topic_data = {
            "id": topic.id,
            "title": topic.title,
            "description": topic.description,
            "introduction": topic.introduction,
            "estimated_duration": topic.estimated_duration,
            "video_url": topic.video_url,
            "video_status": topic.video_status,
            "module": {
                "id": topic.module.id,
                "title": topic.module.title,
                "module_number": topic.module.module_number
            },
            "certification": {
                "id": topic.module.certification.id,
                "name": topic.module.certification.name,
                "slug": topic.module.certification.slug
            },
            "content_sections": {},
            "detailed_content": None
        }
        
        # Add content sections from database
        for section in topic.content_sections:
            json_sections = ["key_points", "practical_examples", "what_to_teach"]
            if section.section_type in json_sections:
                try:
                    content = json.loads(section.content)
                except (json.JSONDecodeError, TypeError):
                    content = section.content
            else:
                content = section.content
            
            topic_data["content_sections"][section.section_type] = content
        
        # Add detailed content from database if available
        if topic.detailed_content:
            try:
                detailed_json = json.loads(topic.detailed_content)
                topic_data["detailed_content"] = detailed_json
            except (json.JSONDecodeError, TypeError):
                topic_data["detailed_content"] = None
        
        return topic_data

    async def search_topics_by_title(
        self,
        db: AsyncSession,
        certification_slug: str,
        title: str
    ) -> List[Dict[str, Any]]:
        """Search for topics by title within a certification"""
        
        stmt = select(SyllabusTopic).join(
            SyllabusModule
        ).join(
            Certification
        ).options(
            selectinload(SyllabusTopic.module)
        ).where(
            and_(
                Certification.slug == certification_slug,
                SyllabusTopic.title.ilike(f"%{title}%"),
                SyllabusTopic.is_active.is_(True)
            )
        ).order_by(
            SyllabusModule.order_index,
            SyllabusTopic.order_index
        )
        
        result = await db.execute(stmt)
        topics = result.scalars().all()
        
        topics_data = []
        for topic in topics:
            topic_data = {
                "id": topic.id,
                "title": topic.title,
                "description": topic.description,
                "module_title": topic.module.title,
                "module_number": topic.module.module_number,
                "estimated_duration": topic.estimated_duration,
                "video_url": topic.video_url,
                "video_status": topic.video_status
            }
            topics_data.append(topic_data)
        
        return topics_data

    def _load_detailed_content_for_topic(self, topic_title: str) -> Optional[Dict]:
        """Load detailed content from seed data files based on topic title"""
        
        # Map topic titles to their corresponding content files
        content_map = {
            "What is System Design?": "what_is_system_design",
            "Why System Design matters": "why_system_design_matters"
        }
        
        if topic_title not in content_map:
            return None
        
        try:
            # Import the content module dynamically
            module_name = content_map[topic_title]
            
            # Path to the seed data content file
            file_path = os.path.join(
                os.path.dirname(__file__),
                "..", "..", "scripts", "seed_data", "certifications",
                "information_technology", "system_design", "syllabus",
                "fundamentals", "topics", f"{module_name}.py"
            )
            
            if not os.path.exists(file_path):
                return None
            
            spec = importlib.util.spec_from_file_location(
                module_name, file_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Return the TOPIC_CONTENT from the module
            return getattr(module, 'TOPIC_CONTENT', None)
            
        except Exception as e:
            # Log error for debugging but don't fail
            print(f"Error loading detailed content for '{topic_title}': {e}")
            return None