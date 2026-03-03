"""Functions for creating test teachers and students"""
from datetime import datetime

# Import from backend root using absolute imports
from models import (
    User,
    TeacherProfile,
    TeacherQualification,
    QuizAttempt,
    TeacherStatus
)
from modules.auth.service import AuthService
from scripts.seed_data.teachers import TEST_TEACHERS, TEST_STUDENTS


async def create_test_teachers(session, certification_map):
    """Create test teachers with their profiles and qualifications"""
    print("👨‍🏫 Creating test teachers...")
    
    auth_service = AuthService()
    teacher_count = 0
    qualification_count = 0
    
    for teacher_data in TEST_TEACHERS:
        # Create user
        password = teacher_data["user"].get(
            "password", "password123"
        )
        user = User(
            id=teacher_data["user"]["id"],
            name=teacher_data["user"]["name"],
            email=teacher_data["user"]["email"],
            email_verified=teacher_data["user"]["email_verified"],
            image=teacher_data["user"]["image"],
            password_hash=auth_service.hash_password(password),
        )
        session.add(user)
        await session.flush()  # To get user ID
        
        # Create teacher profile
        profile_data = teacher_data["profile"]
        
        # Convert string status to enum
        status_str = profile_data["status"]
        if status_str == "approved":
            status_enum = TeacherStatus.APPROVED
        elif status_str == "pending":
            status_enum = TeacherStatus.PENDING
        elif status_str == "rejected":
            status_enum = TeacherStatus.REJECTED
        elif status_str == "suspended":
            status_enum = TeacherStatus.SUSPENDED
        else:
            status_enum = TeacherStatus.PENDING  # Default fallback
            
        profile = TeacherProfile(
            user_id=user.id,
            bio=profile_data["bio"],
            experience_years=profile_data["experience_years"],
            hourly_rate_one_on_one=profile_data["hourly_rate_one_on_one"],
            hourly_rate_group=profile_data["hourly_rate_group"],
            max_group_size=profile_data["max_group_size"],
            status=status_enum,
            is_available=profile_data["is_available"],
            languages_spoken=profile_data["languages_spoken"],
            timezone=profile_data["timezone"],
            approved_at=profile_data["approved_at"],
        )
        session.add(profile)
        await session.flush()  # To get profile ID
        teacher_count += 1
        
        # Create teacher qualifications
        for qual_data in teacher_data["qualifications"]:
            cert_slug = qual_data["certification_slug"]
            if cert_slug in certification_map:
                certification = certification_map[cert_slug]
                
                # Create a mock quiz attempt
                quiz_attempt = QuizAttempt(
                    id=f"test_attempt_{user.id}_{cert_slug}",
                    user_id=user.id,
                    certification_id=certification.id,
                    score=int(qual_data["score_percentage"]),
                    total_questions=100,
                    correct_answers=int(qual_data["score_percentage"]),
                    points=int(qual_data["score_percentage"]),
                    completed_at=datetime.now(),
                )
                session.add(quiz_attempt)
                await session.flush()
                
                # Create teacher qualification
                qualification = TeacherQualification(
                    user_id=user.id,
                    category_id=certification.category_id,
                    certification_id=certification.id,
                    quiz_attempt_id=quiz_attempt.id,
                    score_percentage=qual_data["score_percentage"],
                )
                session.add(qualification)
                qualification_count += 1
    
    print(f"✅ Created {teacher_count} test teachers with "
          f"{qualification_count} qualifications")


async def create_test_students(session):
    """Create test students"""
    print("👨‍🎓 Creating test students...")
    
    auth_service = AuthService()
    student_count = 0
    
    for student_data in TEST_STUDENTS:
        # Create user
        password = student_data.get("password", "student123")
        user = User(
            id=student_data["id"],
            name=student_data["name"],
            email=student_data["email"],
            email_verified=student_data["email_verified"],
            image=student_data["image"],
            password_hash=auth_service.hash_password(password),
        )
        session.add(user)
        student_count += 1
    
    print(f"✅ Created {student_count} test students")
