import asyncio
import sys
import os
from datetime import datetime
from uuid import uuid4
import importlib

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import engine, AsyncSessionLocal
from models import Base, Category, Certification, Question, Answer

# Import seed data
from seed_data.categories import CATEGORIES
from seed_data.certifications import aws, azure, google_cloud, devops, programming, cybersecurity, data_analytics, project_management, networking, database

# Collect all certification modules
CERTIFICATION_MODULES = [
    aws, azure, google_cloud, devops, programming, 
    cybersecurity, data_analytics, project_management, networking, database
]

async def seed_database():
    """Seed the database with comprehensive certification data"""
    print("🌱 Starting comprehensive database seeding...")
    print(f"📊 Seeding {len(CATEGORIES)} categories with 30+ certifications")
    
    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created")
    
    async with AsyncSessionLocal() as session:
        try:
            # Create categories
            print("📁 Creating categories...")
            category_map = {}
            for category_data in CATEGORIES:
                category = Category(
                    name=category_data["name"],
                    description=category_data["description"],
                    slug=category_data["slug"],
                    icon=category_data["icon"],
                    color=category_data["color"]
                )
                session.add(category)
                category_map[category_data["slug"]] = category
            
            await session.flush()  # To get category IDs
            print(f"✅ Created {len(CATEGORIES)} categories")
            
            # Create certifications from all modules
            print("📜 Creating certifications...")
            certification_map = {}
            total_certifications = 0
            
            for module in CERTIFICATION_MODULES:
                module_certifications = 0
                for cert_data in module.CERTIFICATIONS:
                    category = category_map[cert_data["category_slug"]]
                    
                    certification = Certification(
                        name=cert_data["name"],
                        description=cert_data["description"],
                        slug=cert_data["slug"],
                        level=cert_data["level"],
                        duration=cert_data["duration"],
                        questions_count=cert_data["questions_count"],
                        category_id=category.id,
                        is_active=cert_data["is_active"]
                    )
                    session.add(certification)
                    certification_map[cert_data["slug"]] = certification
                    module_certifications += 1
                    total_certifications += 1
                
                print(f"  📋 {module.__name__.split('.')[-1]}: {module_certifications} certifications")
            
            await session.flush()  # To get certification IDs
            print(f"✅ Created {total_certifications} certifications")
            
            # Create questions and answers
            print("❓ Creating questions and answers...")
            total_questions = 0
            total_answers = 0
            
            for module in CERTIFICATION_MODULES:
                if hasattr(module, 'QUESTIONS'):
                    for cert_slug, questions_data in module.QUESTIONS.items():
                        if cert_slug in certification_map:
                            certification = certification_map[cert_slug]
                            
                            for question_data in questions_data:
                                question = Question(
                                    text=question_data["text"],
                                    explanation=question_data["explanation"],
                                    reference=question_data.get("reference", ""),
                                    points=question_data.get("points", 1),
                                    certification_id=certification.id
                                )
                                session.add(question)
                                await session.flush()  # To get question ID
                                total_questions += 1
                                
                                for answer_data in question_data["answers"]:
                                    answer = Answer(
                                        text=answer_data["text"],
                                        is_correct=answer_data["is_correct"],
                                        question_id=question.id
                                    )
                                    session.add(answer)
                                    total_answers += 1
            
            print(f"✅ Created {total_questions} questions with {total_answers} answer options")
            
            # Commit all changes
            await session.commit()
            
            # Print summary
            print("\n🎉 Database seeding completed successfully!")
            print("=" * 50)
            print("SEEDING SUMMARY:")
            print(f"📁 Categories: {len(CATEGORIES)}")
            print(f"📜 Certifications: {total_certifications}")
            print(f"❓ Questions: {total_questions}")
            print(f"✅ Answer Options: {total_answers}")
            print("=" * 50)
            
            # Print breakdown by category
            print("\nCERTIFICATIONS BY CATEGORY:")
            for category_data in CATEGORIES:
                category = category_map[category_data["slug"]]
                cert_count = sum(1 for module in CERTIFICATION_MODULES 
                               for cert in module.CERTIFICATIONS 
                               if cert["category_slug"] == category_data["slug"])
                print(f"  {category_data['name']}: {cert_count} certifications")
            
        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            await session.rollback()
            raise

if __name__ == "__main__":
    asyncio.run(seed_database())
