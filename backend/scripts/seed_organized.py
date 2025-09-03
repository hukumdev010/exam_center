import asyncio
import sys
import os
from datetime import datetime
from uuid import uuid4
import importlib
import glob

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import engine, AsyncSessionLocal
from models import Base, Category, Certification, Question, Answer

# Import seed data
from seed_data.categories import CATEGORIES

def load_all_certifications():
    """Dynamically load all certifications from the organized folder structure"""
    certifications_root = os.path.join(os.path.dirname(__file__), 'seed_data', 'certifications')
    all_certifications = []
    all_questions = {}
    
    # Get all category folders
    category_folders = [f for f in os.listdir(certifications_root) 
                       if os.path.isdir(os.path.join(certifications_root, f)) and not f.startswith('__')]
    
    for category_folder in category_folders:
        try:
            # Try to import the category module (organized structure)
            module_path = f'seed_data.certifications.{category_folder}'
            category_module = importlib.import_module(module_path)
            
            if hasattr(category_module, 'CERTIFICATIONS'):
                all_certifications.extend(category_module.CERTIFICATIONS)
                print(f"  📋 {category_folder}: {len(category_module.CERTIFICATIONS)} certifications loaded")
                
                if hasattr(category_module, 'ALL_QUESTIONS'):
                    all_questions.update(category_module.ALL_QUESTIONS)
                    
        except ImportError as e:
            print(f"  ⚠️  {category_folder}: No organized module found, trying individual files")
            
            # Fallback: try to load individual certification files
            category_path = os.path.join(certifications_root, category_folder)
            cert_files = glob.glob(os.path.join(category_path, '*.py'))
            
            category_certs = []
            category_questions = {}
            
            for cert_file in cert_files:
                if os.path.basename(cert_file).startswith('__'):
                    continue
                    
                try:
                    cert_module_name = os.path.splitext(os.path.basename(cert_file))[0]
                    cert_module_path = f'seed_data.certifications.{category_folder}.{cert_module_name}'
                    cert_module = importlib.import_module(cert_module_path)
                    
                    if hasattr(cert_module, 'CERTIFICATION'):
                        category_certs.append(cert_module.CERTIFICATION)
                        
                        if hasattr(cert_module, 'QUESTIONS') and cert_module.QUESTIONS:
                            category_questions[cert_module.CERTIFICATION['slug']] = cert_module.QUESTIONS
                            
                except ImportError as cert_e:
                    print(f"    ❌ Failed to load {cert_module_name}: {cert_e}")
            
            if category_certs:
                all_certifications.extend(category_certs)
                all_questions.update(category_questions)
                print(f"  📋 {category_folder}: {len(category_certs)} certifications loaded (individual files)")
    
    # Load legacy flat files only for categories that don't have organized structure
    try:
        # Only load legacy modules that don't have organized counterparts
        legacy_modules = []
        for module_name in ['azure', 'google_cloud', 'devops', 'programming', 'data_analytics', 'project_management', 'networking', 'database']:
            if module_name not in category_folders:
                try:
                    module = importlib.import_module(f'seed_data.certifications.{module_name}')
                    legacy_modules.append((module_name, module))
                except ImportError:
                    continue
        
        for module_name, module in legacy_modules:
            if hasattr(module, 'CERTIFICATIONS'):
                all_certifications.extend(module.CERTIFICATIONS)
                print(f"  📋 {module_name} (legacy): {len(module.CERTIFICATIONS)} certifications")
                
                if hasattr(module, 'QUESTIONS'):
                    all_questions.update(module.QUESTIONS)
                    
    except ImportError as e:
        print(f"  ℹ️  No legacy certification modules found: {e}")
    
    return all_certifications, all_questions

async def seed_database():
    """Seed the database with comprehensive certification data"""
    print("🌱 Starting comprehensive database seeding with organized structure...")
    
    # Load all certifications dynamically
    print("📂 Loading certifications from organized folder structure...")
    all_certifications, all_questions = load_all_certifications()
    
    print(f"📊 Found {len(CATEGORIES)} categories and {len(all_certifications)} certifications")
    
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
            
            # Create certifications
            print("📜 Creating certifications...")
            certification_map = {}
            
            for cert_data in all_certifications:
                category_slug = cert_data["category_slug"]
                if category_slug in category_map:
                    category = category_map[category_slug]
                    
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
                else:
                    print(f"  ⚠️  Skipping certification {cert_data['name']} - category '{category_slug}' not found")
            
            await session.flush()  # To get certification IDs
            print(f"✅ Created {len(certification_map)} certifications")
            
            # Create questions and answers
            print("❓ Creating questions and answers...")
            total_questions = 0
            total_answers = 0
            
            for cert_slug, questions_data in all_questions.items():
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
            print("=" * 60)
            print("SEEDING SUMMARY:")
            print(f"📁 Categories: {len(CATEGORIES)}")
            print(f"📜 Certifications: {len(certification_map)}")
            print(f"❓ Questions: {total_questions}")
            print(f"✅ Answer Options: {total_answers}")
            print("=" * 60)
            
            # Print breakdown by category
            print("\nCERTIFICATIONS BY CATEGORY:")
            for category_data in CATEGORIES:
                cert_count = sum(1 for cert in all_certifications 
                               if cert["category_slug"] == category_data["slug"])
                print(f"  {category_data['name']}: {cert_count} certifications")
            
        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            await session.rollback()
            raise

if __name__ == "__main__":
    asyncio.run(seed_database())
