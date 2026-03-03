"""
Script to update syllabus topics with detailed comprehensive content from seed data files.
This script loads the detailed content from topic files and updates the database.
"""

import asyncio
import sys
import json
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent.parent
sys.path.append(str(backend_path))

from database import get_db
from models import Certification, SyllabusTopic, SyllabusModule
from sqlalchemy import select
from sqlalchemy.orm import selectinload


async def update_topic_detailed_content():
    """Update topics with detailed content from seed data files"""
    
    db_gen = get_db()
    db = await db_gen.__anext__()
    
    try:
        # Import the detailed content from our files
        sys.path.append(str(Path(__file__).parent / "seed_data" / "certifications" / 
                           "information_technology" / "system_design" / "syllabus" / 
                           "fundamentals" / "topics"))
        
        # Import the content modules
        try:
            import what_is_system_design
            import why_system_design_matters
            import common_architecture_patterns
            import scalability_fundamentals
            
            content_map = {
                "What is System Design?": what_is_system_design.TOPIC_CONTENT,
                "Why System Design matters": why_system_design_matters.TOPIC_CONTENT,
                "Common Architecture Patterns": common_architecture_patterns.TOPIC_CONTENT,
                "Scalability Fundamentals": scalability_fundamentals.TOPIC_CONTENT
            }
            
        except ImportError as e:
            print(f"❌ Error importing content files: {e}")
            return
        
        # Get the certification
        stmt = select(Certification).options(
            selectinload(Certification.syllabus_modules).options(
                selectinload(SyllabusModule.topics)
            )
        ).where(
            Certification.slug == "system-design-fundamentals"
        )
        result = await db.execute(stmt)
        certification = result.scalar_one_or_none()
        
        if not certification:
            print("❌ System Design Fundamentals certification not found!")
            return
        
        print(f"✅ Found certification: {certification.name}")
        
        updated_count = 0
        
        # Update topics with detailed content
        for module in certification.syllabus_modules:
            for topic in module.topics:
                if topic.title in content_map:
                    detailed_content = content_map[topic.title]
                    
                    # Convert the content to JSON string
                    topic.detailed_content = json.dumps(detailed_content, indent=2)
                    
                    print(f"✅ Updated detailed content for: {topic.title}")
                    updated_count += 1
                else:
                    print(f"⚠️  No detailed content found for: {topic.title}")
        
        await db.commit()
        print(f"\n🎉 Successfully updated {updated_count} topics with detailed content!")
        
        # Verify the updates
        print("\n📋 Verification:")
        for module in certification.syllabus_modules:
            for topic in module.topics:
                has_detailed = bool(topic.detailed_content)
                status = "✅" if has_detailed else "❌"
                print(f"  {status} {topic.title}: {'Has' if has_detailed else 'Missing'} detailed content")
    
    except Exception as e:
        print(f"❌ Error updating detailed content: {e}")
        import traceback
        traceback.print_exc()
        await db.rollback()
    
    finally:
        await db.close()


async def verify_detailed_content():
    """Verify that detailed content is properly stored and can be retrieved"""
    
    db_gen = get_db()
    db = await db_gen.__anext__()
    
    try:
        # Get topics with detailed content
        stmt = select(SyllabusTopic).join(SyllabusModule).join(Certification).where(
            Certification.slug == "system-design-fundamentals"
        ).options(
            selectinload(SyllabusTopic.module)
        )
        
        result = await db.execute(stmt)
        topics = result.scalars().all()
        
        print("\n🔍 Detailed Content Verification:")
        print("="*50)
        
        for topic in topics:
            print(f"\n📝 Topic: {topic.title}")
            print(f"   Module: {topic.module.title}")
            
            if topic.detailed_content:
                try:
                    content = json.loads(topic.detailed_content)
                    print(f"   ✅ Has detailed content ({len(topic.detailed_content)} characters)")
                    print(f"   📖 Title: {content.get('title', 'N/A')}")
                    print(f"   ⏱️  Duration: {content.get('duration', 'N/A')}")
                    print(f"   📊 Difficulty: {content.get('difficulty', 'N/A')}")
                    
                    # Show structure overview
                    if 'detailed_content' in content:
                        sections = list(content['detailed_content'].keys())
                        print(f"   📋 Sections: {', '.join(sections[:3])}{'...' if len(sections) > 3 else ''}")
                    
                except json.JSONDecodeError:
                    print(f"   ❌ Invalid JSON content")
            else:
                print(f"   ❌ No detailed content")
    
    except Exception as e:
        print(f"❌ Error verifying content: {e}")
    
    finally:
        await db.close()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Update or verify detailed topic content')
    parser.add_argument('--verify', action='store_true', help='Verify existing content')
    args = parser.parse_args()
    
    if args.verify:
        asyncio.run(verify_detailed_content())
    else:
        asyncio.run(update_topic_detailed_content())