"""Syllabus API routes"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, List, Any

from database import get_db
from modules.syllabus.service import SyllabusService

router = APIRouter(prefix="/api/syllabus", tags=["syllabus"])


@router.get("/topics/{certification_slug}/video-ready")
async def get_topics_for_video_creation(
    certification_slug: str,
    status: str = "planned",
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get topics that need video creation with detailed content for YouTube video production"""
    
    try:
        syllabus_service = SyllabusService()
        topics = await syllabus_service.get_topics_for_video_creation(
            db, certification_slug, status
        )
        
        return {
            "certification_slug": certification_slug,
            "video_status": status,
            "total_topics": len(topics),
            "topics": topics
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get topics for video creation: {str(e)}"
        )


@router.put("/topics/{topic_id}/video-status")
async def update_topic_video_status(
    topic_id: int,
    video_url: str = None,
    status: str = "planned",
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Update video status and URL for a topic"""
    
    try:
        syllabus_service = SyllabusService()
        success = await syllabus_service.update_topic_video_status(
            db, topic_id, video_url, status
        )
        
        if success:
            return {
                "topic_id": topic_id,
                "video_url": video_url,
                "status": status,
                "message": "Video status updated successfully"
            }
        else:
            raise HTTPException(
                status_code=404,
                detail="Topic not found"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to update video status: {str(e)}"
        )


@router.get("/{certification_slug}/structured")
async def get_structured_syllabus(
    certification_slug: str,
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get structured syllabus data with detailed content for each topic"""
    
    try:
        syllabus_service = SyllabusService()
        syllabus = await syllabus_service.get_certification_syllabus_structured(
            db, certification_slug
        )
        
        if not syllabus:
            raise HTTPException(
                status_code=404,
                detail="Syllabus not found for this certification"
            )
            
        return syllabus
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get structured syllabus: {str(e)}"
        )


@router.get("/topics/{topic_id}/content")
async def get_topic_content_details(
    topic_id: int,
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get detailed content for a specific topic including comprehensive learning material"""
    
    try:
        syllabus_service = SyllabusService()
        topic_content = await syllabus_service.get_topic_detailed_content(
            db, topic_id
        )
        
        if not topic_content:
            raise HTTPException(
                status_code=404,
                detail="Topic not found or no detailed content available"
            )
            
        return topic_content
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get topic content: {str(e)}"
        )


@router.get("/topics/search")
async def search_topics_by_title(
    certification_slug: str,
    title: str,
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Search for topics by title within a certification"""
    
    try:
        syllabus_service = SyllabusService()
        topics = await syllabus_service.search_topics_by_title(
            db, certification_slug, title
        )
        
        return {
            "certification_slug": certification_slug,
            "search_title": title,
            "total_results": len(topics),
            "topics": topics
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to search topics: {str(e)}"
        )