from typing import Optional
from sqlalchemy import select, and_
from sqlalchemy import desc as sql_desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models import (
    User, QuizAttempt, UserProgress, Certification, Category,
    TeacherQualification, TeacherProfile
)
from .model import (
    UserActivityItem, UserActivity, UserQualifications, UserQualification
)


class UserService:
    
    @staticmethod
    async def get_user_profile(
        db: AsyncSession, user_id: str
    ) -> Optional[User]:
        """Get user profile by ID"""
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_user_activity(
        db: AsyncSession,
        user_id: str,
        limit: int = 10
    ) -> UserActivity:
        """Get user's recent activity (quiz attempts and progress updates)"""
        
        # Get quiz attempts
        quiz_result = await db.execute(
            select(QuizAttempt, Certification.name.label('cert_name'))
            .join(Certification,
                  QuizAttempt.certification_id == Certification.id)
            .where(QuizAttempt.user_id == user_id)
            .order_by(sql_desc(QuizAttempt.created_at))
            .limit(limit)
        )
        quiz_attempts = quiz_result.fetchall()

        # Get progress updates
        progress_result = await db.execute(
            select(UserProgress, Certification.name.label('cert_name'))
            .join(Certification,
                  UserProgress.certification_id == Certification.id)
            .where(UserProgress.user_id == user_id)
            .order_by(sql_desc(UserProgress.updated_at))
            .limit(limit)
        )
        progress_updates = progress_result.fetchall()
        
        # Combine and sort activities
        activities = []
        
        # Add quiz attempts
        for attempt, cert_name in quiz_attempts:
            desc = (
                f"Scored {attempt.score}% "
                f"({attempt.correct_answers}/{attempt.total_questions})"
            )
            activities.append(UserActivityItem(
                id=attempt.id,
                type="quiz_attempt",
                title=f"Quiz Attempt: {cert_name}",
                description=desc,
                score=attempt.score,
                certification_name=cert_name,
                certification_id=attempt.certification_id,
                points=attempt.points,
                created_at=attempt.created_at
            ))

        # Add progress updates
        for progress, cert_name in progress_updates:
            prog_id = (f"progress_{progress.user_id}_"
                       f"{progress.certification_id}")
            # Calculate progress percentage
            progress_percentage = round((progress.current_question / progress.total_questions) * 100, 1) if progress.total_questions > 0 else 0
            desc = f"Progress: {progress_percentage}% completed"
            activities.append(UserActivityItem(
                id=prog_id,
                type="progress_update",
                title=f"Progress Update: {cert_name}",
                description=desc,
                certification_name=cert_name,
                certification_id=progress.certification_id,
                created_at=progress.updated_at
            ))
        
        # Sort by date (most recent first) and limit
        activities.sort(key=lambda x: x.created_at, reverse=True)
        activities = activities[:limit]
        
        # Get total count for pagination
        total_quiz_count_result = await db.execute(
            select(QuizAttempt).where(QuizAttempt.user_id == user_id)
        )
        total_quiz_count = len(total_quiz_count_result.fetchall())
        
        total_progress_count_result = await db.execute(
            select(UserProgress).where(UserProgress.user_id == user_id)
        )
        total_progress_count = len(total_progress_count_result.fetchall())
        
        total_count = total_quiz_count + total_progress_count
        
        return UserActivity(
            activities=activities,
            total_count=total_count
        )

    @staticmethod
    async def create_or_update_user(
        db: AsyncSession, user_info: dict
    ) -> User:
        """Create a new user or update existing user from OAuth data"""
        
        # Try to find existing user by email
        existing_user_result = await db.execute(
            select(User).where(User.email == user_info.get("email"))
        )
        existing_user = existing_user_result.scalar_one_or_none()
        
        if existing_user:
            # Update existing user's information
            existing_user.name = user_info.get("name", existing_user.name)
            existing_user.image = user_info.get("picture", existing_user.image)
            # Update email verification if not set
            if (
                not existing_user.email_verified
                and user_info.get("verified_email")
            ):
                from datetime import datetime
                existing_user.email_verified = datetime.utcnow()
            
            await db.commit()
            await db.refresh(existing_user)
            return existing_user
        else:
            # Create new user
            new_user = User(
                id=user_info.get("id"),
                name=user_info.get("name"),
                email=user_info.get("email"),
                image=user_info.get("picture")
            )
            
            # Set email verification if verified
            if user_info.get("verified_email"):
                from datetime import datetime
                new_user.email_verified = datetime.utcnow()
            
            try:
                db.add(new_user)
                await db.commit()
                await db.refresh(new_user)
                return new_user
            except IntegrityError:
                # Handle race condition where user was created by
                # another request
                await db.rollback()
                # Try to fetch the user that was just created
                result = await db.execute(
                    select(User).where(User.email == user_info.get("email"))
                )
                return result.scalar_one()

    @staticmethod
    async def get_user_qualifications(
        db: AsyncSession, user_id: str
    ) -> UserQualifications:
        """Get user's passed certifications that can qualify for teaching"""
        
        # Get all quiz attempts with score >= 80% (certificate eligible)
        query = (
            select(
                QuizAttempt,
                Certification.name.label('cert_name'),
                Category.name.label('category_name')
            )
            .join(Certification, QuizAttempt.certification_id == Certification.id)
            .join(Category, Certification.category_id == Category.id)
            .where(
                and_(
                    QuizAttempt.user_id == user_id,
                    QuizAttempt.score >= 80  # Must pass to be qualified
                )
            )
            .order_by(sql_desc(QuizAttempt.completed_at))
        )
        
        result = await db.execute(query)
        quiz_attempts = result.fetchall()
        
        # Get existing teacher qualifications to check if user is already teaching
        teacher_qualifications = await db.execute(
            select(TeacherQualification)
            .where(TeacherQualification.user_id == user_id)
        )
        existing_qualifications = {
            tq.certification_id: tq for tq in teacher_qualifications.scalars().all()
        }
        
        # Check if user has teacher profile
        teacher_profile = await db.execute(
            select(TeacherProfile)
            .where(TeacherProfile.user_id == user_id)
        )
        has_teacher_profile = teacher_profile.scalar_one_or_none() is not None
        
        qualifications = []
        seen_certifications = set()  # To handle multiple attempts for same cert
        
        for attempt, cert_name, category_name in quiz_attempts:
            # Only include the highest score attempt for each certification
            if attempt.certification_id in seen_certifications:
                continue
            seen_certifications.add(attempt.certification_id)
            
            can_teach = attempt.score >= 90  # Must score 90%+ to teach
            is_teaching = (
                has_teacher_profile and 
                attempt.certification_id in existing_qualifications
            )
            
            qualifications.append(UserQualification(
                id=attempt.id,
                certification_name=cert_name,
                category_name=category_name,
                score=attempt.score,
                qualified_at=attempt.completed_at,
                can_teach=can_teach,
                is_teaching=is_teaching
            ))
        
        return UserQualifications(
            qualifications=qualifications,
            total_count=len(qualifications)
        )