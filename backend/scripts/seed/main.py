import asyncio
# Import from backend root using absolute imports
from database import AsyncSessionLocal, engine
from models import (
    Answer, Base, Category, Certification, Question
)
from scripts.seed.test_users import create_test_teachers, create_test_students
from scripts.seed_data.teachers import TEST_TEACHERS, TEST_STUDENTS
from scripts.seed.discovery import auto_discover_categories_and_certifications
from scripts.seed.syllabus_functions import (
    create_system_design_syllabus,
    create_frontend_react_syllabus,
    populate_detailed_content,
    populate_frontend_detailed_content
)


async def seed_database():
    """Seed the database with auto-discovered certification data"""
    print("🌱 Starting database seeding with auto-discovery...")

    # Auto-discover all certifications and categories
    discovered_data = auto_discover_categories_and_certifications()
    
    categories_data = list(discovered_data["categories"].values())
    all_certifications = discovered_data["certifications"]
    all_questions = discovered_data["questions"]
    
    # Deduplicate certifications by slug
    seen_slugs = set()
    unique_certifications = []
    for cert in all_certifications:
        slug = cert.get("slug")
        if slug and slug not in seen_slugs:
            seen_slugs.add(slug)
            unique_certifications.append(cert)
        else:
            print(f"  ⚠️  Skipping duplicate certification slug: {slug}")
    
    all_certifications = unique_certifications

    print(
        f"📊 Found {len(categories_data)} categories and "
        f"{len(all_certifications)} certifications"
    )

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created")

    async with AsyncSessionLocal() as session:
        try:
            # Create categories with hierarchy support
            print("📁 Creating categories...")
            category_map = {}
            
            # Sort categories by level to ensure parents are created first
            categories_data.sort(key=lambda x: x["level"])
            
            # First pass: create all categories without parent relationships
            for category_data in categories_data:
                category = Category(
                    name=category_data["name"],
                    description=category_data["description"],
                    slug=category_data["slug"],
                    icon=category_data.get("icon", "book"),
                    color=category_data.get("color", "gray"),
                )
                session.add(category)
                category_map[category_data["slug"]] = category

            await session.flush()  # To get category IDs
            
            # Second pass: set parent relationships
            for category_data in categories_data:
                if category_data.get("parent_slug"):
                    parent_slug = category_data["parent_slug"]
                    if parent_slug in category_map:
                        child_category = category_map[category_data["slug"]]
                        parent_category = category_map[parent_slug]
                        child_category.parent_id = parent_category.id
            
            await session.flush()  # Update parent relationships
            print(
                f"✅ Created {len(categories_data)} categories with hierarchy"
                )

            # Create certifications
            print("📜 Creating certifications...")
            certification_map = {}

            for cert_data in all_certifications:
                category_slug = cert_data["category_slug"]
                if category_slug in category_map:
                    category = category_map[category_slug]

                    certification = Certification(
                        name=cert_data.get("name", "Unknown Certification"),
                        description=cert_data.get("description", " "),
                        slug=cert_data.get("slug", "unknown-cert"),
                        level=cert_data.get("level", "Beginner"),
                        duration=cert_data.get("duration", 60),
                        questions_count=cert_data.get("questions_count", 10),
                        category_id=category.id,
                        is_active=cert_data.get("is_active", True),
                        benefits=cert_data.get("benefits"),
                        advantages=cert_data.get("advantages"),
                        career_benefits=cert_data.get("career_benefits"),
                        teaching_eligibility=cert_data.get(
                            "teaching_eligibility", False
                        ),
                        min_score_for_teaching=cert_data.get(
                            "min_score_for_teaching", 90
                        ),
                        min_score_for_certificate=cert_data.get(
                            "min_score_for_certificate", 80
                        ),
                        syllabus=cert_data.get("syllabus"),
                    )
                    session.add(certification)
                    certification_map[cert_data["slug"]] = certification
                else:
                    cert_name = cert_data.get("name", "Unknown")
                    print(
                        f"  ⚠️  Skipping certification {cert_name} - "
                        f"category '{category_slug}' not found"
                    )

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
                        # Ensure question has required fields
                        if not question_data.get("text"):
                            print(
                                f"    ⚠️  Skipping question without "
                                f"text for {cert_slug}"
                            )
                            continue
                            
                        question = Question(
                            text=question_data.get("text", ""),
                            explanation=question_data.get("explanation", ""),
                            reference=question_data.get("reference", ""),
                            points=question_data.get("points", 1),
                            certification_id=certification.id,
                        )
                        session.add(question)
                        await session.flush()  # To get question ID
                        total_questions += 1

                        # Process answers if they exist
                        answers = question_data.get("answers", [])
                        for answer_data in answers:
                            if not answer_data.get("text"):
                                continue
                                
                            answer = Answer(
                                text=answer_data.get("text", ""),
                                is_correct=answer_data.get(
                                    "is_correct", False
                                ),
                                question_id=question.id,
                            )
                            session.add(answer)
                            total_answers += 1

            print(
                f"✅ Created {total_questions} questions with "
                f"{total_answers} answer options"
            )

            # Create test teachers with their profiles and qualifications
            await create_test_teachers(session, certification_map)

            # Create test students
            await create_test_students(session)

            # Create syllabus structure for System Design Fundamentals
            await create_system_design_syllabus(session, certification_map)

            # Create syllabus structure for Frontend React Fundamentals
            await create_frontend_react_syllabus(session, certification_map)

            # Populate detailed content for Frontend syllabus topics
            await populate_frontend_detailed_content(session)

            # Populate detailed content for System Design syllabus topics
            await populate_detailed_content(session)

            # Commit all changes
            await session.commit()

            # Print summary
            print("\n🎉 Database seeding completed successfully!")
            print("=" * 60)
            print("SEEDING SUMMARY:")
            print(f"📁 Categories: {len(categories_data)}")
            print(f"📜 Certifications: {len(certification_map)}")
            print(f"❓ Questions: {total_questions}")
            print(f"✅ Answer Options: {total_answers}")
            print(f"👨‍🏫 Test Teachers: {len(TEST_TEACHERS)}")
            print(f"👨‍🎓 Test Students: {len(TEST_STUDENTS)}")
            print("=" * 60)

            # Print breakdown by category
            print("\nCERTIFICATIONS BY CATEGORY:")
            for category_data in categories_data:
                cert_count = sum(
                    1
                    for cert in all_certifications
                    if cert["category_slug"] == category_data["slug"]
                )
                cert_name = category_data['name']
                print(f"  {cert_name}: {cert_count} certifications")

        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            await session.rollback()
            raise


if __name__ == "__main__":
    asyncio.run(seed_database())
