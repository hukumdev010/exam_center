from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, and_, or_, desc
from models import (
    TeacherProfile,
    TeacherQualification,
    User,
    QuizAttempt,
    Certification,
    TeacherStatus
)
from .model import (
    TeacherProfileCreate,
    TeacherProfileUpdate,
    AdminApprovalRequest,
    TeacherStatusEnum
)
from datetime import datetime


class TeacherService:
    
    @staticmethod
    async def create_quiz_qualification(
        db: AsyncSession,
        user_id: str,
        quiz_attempt_id: str
    ) -> Optional[TeacherQualification]:
        """
        Create a teacher qualification if user scored 90% or above
        """
        # Get the quiz attempt
        stmt = select(QuizAttempt).where(
            and_(
                QuizAttempt.id == quiz_attempt_id,
                QuizAttempt.user_id == user_id
            )
        ).options(selectinload(QuizAttempt.certification))
        
        result = await db.execute(stmt)
        quiz_attempt = result.scalar_one_or_none()
        
        if not quiz_attempt:
            return None
            
        # Calculate percentage
        score_percentage = (
            quiz_attempt.correct_answers / quiz_attempt.total_questions
        ) * 100
        
        # Must be 90% or above to qualify
        if score_percentage < 90.0:
            return None
            
        # Check if qualification already exists
        existing_stmt = select(TeacherQualification).where(
            and_(
                TeacherQualification.user_id == user_id,
                TeacherQualification.certification_id == (
                    quiz_attempt.certification_id
                )
            )
        )
        existing_result = await db.execute(existing_stmt)
        if existing_result.scalar_one_or_none():
            return None  # Already qualified
            
        # Create qualification
        qualification = TeacherQualification(
            user_id=user_id,
            category_id=quiz_attempt.certification.category_id,
            certification_id=quiz_attempt.certification_id,
            quiz_attempt_id=quiz_attempt_id,
            score_percentage=score_percentage,
            is_active=True,
            qualified_at=datetime.utcnow()
        )
        
        db.add(qualification)
        await db.commit()
        await db.refresh(qualification)
        
        return qualification

    @staticmethod
    async def create_teacher_profile(
        db: AsyncSession,
        user_id: str,
        profile_data: TeacherProfileCreate
    ) -> TeacherProfile:
        """
        Create a teacher profile (requires admin approval)
        """
        # Check if user has any qualifications
        qualifications_stmt = select(TeacherQualification).where(
            and_(
                TeacherQualification.user_id == user_id,
                TeacherQualification.is_active
            )
        )
        result = await db.execute(qualifications_stmt)
        qualifications = result.scalars().all()
        
        if not qualifications:
            raise ValueError(
                (
                    "User must have at least one qualification (90%+ score) "
                    "to apply as teacher"
                )
            )
            
        # Check if profile already exists
        existing_stmt = select(TeacherProfile).where(
            TeacherProfile.user_id == user_id
        )
        existing_result = await db.execute(existing_stmt)
        if existing_result.scalar_one_or_none():
            raise ValueError("Teacher profile already exists for this user")
            
        teacher_profile = TeacherProfile(
            user_id=user_id,
            bio=profile_data.bio,
            qualifications=profile_data.qualifications,
            experience=profile_data.experience,
            github_url=profile_data.github_url,
            linkedin_url=profile_data.linkedin_url,
            website_url=profile_data.website_url,
            experience_years=profile_data.experience_years,
            hourly_rate_one_on_one=profile_data.hourly_rate_one_on_one,
            hourly_rate_group=profile_data.hourly_rate_group,
            max_group_size=profile_data.max_group_size,
            status=TeacherStatus.PENDING,
            is_available=True,
            languages_spoken=profile_data.languages_spoken,
            timezone=profile_data.timezone
        )
        
        db.add(teacher_profile)
        await db.commit()
        await db.refresh(teacher_profile)
        
        return teacher_profile

    @staticmethod
    async def update_teacher_profile(
        db: AsyncSession,
        user_id: str,
        update_data: TeacherProfileUpdate
    ) -> Optional[TeacherProfile]:
        """
        Update teacher profile (only by the teacher themselves)
        """
        stmt = select(TeacherProfile).where(TeacherProfile.user_id == user_id)
        result = await db.execute(stmt)
        teacher_profile = result.scalar_one_or_none()
        
        if not teacher_profile:
            return None
            
        # Update fields
        for field, value in update_data.model_dump(exclude_unset=True).items():
            setattr(teacher_profile, field, value)
            
        teacher_profile.updated_at = datetime.utcnow()
        
        await db.commit()
        await db.refresh(teacher_profile)
        
        return teacher_profile

    @staticmethod
    async def admin_approve_teacher(
        db: AsyncSession,
        teacher_id: int,
        admin_user_id: str,
        approval_data: AdminApprovalRequest
    ) -> Optional[TeacherProfile]:
        """
        Admin approval/rejection of teacher application
        """
        stmt = select(TeacherProfile).where(TeacherProfile.id == teacher_id)
        result = await db.execute(stmt)
        teacher_profile = result.scalar_one_or_none()
        
        if not teacher_profile:
            return None
            
        teacher_profile.status = TeacherStatus(approval_data.status.value)
        
        if approval_data.status == TeacherStatusEnum.APPROVED:
            teacher_profile.approved_by = admin_user_id
            teacher_profile.approved_at = datetime.utcnow()
            teacher_profile.rejection_reason = None
        elif approval_data.status == TeacherStatusEnum.REJECTED:
            teacher_profile.rejection_reason = approval_data.rejection_reason
            teacher_profile.approved_by = admin_user_id
            teacher_profile.approved_at = None
            
        # Set admin notes if provided
        if approval_data.admin_notes:
            teacher_profile.admin_notes = approval_data.admin_notes
            
        teacher_profile.updated_at = datetime.utcnow()
        
        await db.commit()
        await db.refresh(teacher_profile)
        
        return teacher_profile

    @staticmethod
    async def get_teacher_profile(
        db: AsyncSession,
        user_id: str
    ) -> Optional[TeacherProfile]:
        """
        Get teacher profile by user ID
        """
        stmt = select(TeacherProfile).where(TeacherProfile.user_id == user_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def get_teacher_with_qualifications(
        db: AsyncSession,
        user_id: str
    ) -> Optional[TeacherProfile]:
        """
        Get teacher profile with qualifications
        """
        stmt = select(TeacherProfile).where(
            TeacherProfile.user_id == user_id
        ).options(
            selectinload(TeacherProfile.user),
            selectinload(TeacherProfile.user).selectinload(
                User.teacher_qualifications
            )
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def list_teachers(
        db: AsyncSession,
        query: Optional[str] = None,
        status: Optional[TeacherStatusEnum] = None,
        is_available: Optional[bool] = None,
        category_id: Optional[int] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[TeacherProfile]:
        """
        List teachers with filters
        """
        stmt = select(TeacherProfile).options(
            selectinload(TeacherProfile.user)
        )
        
        conditions = []
        
        # Add search filter if query is provided
        if query:
            # Join with User table for name search
            stmt = stmt.join(User, TeacherProfile.user_id == User.id)
            
            search_filter = or_(
                User.first_name.ilike(f"%{query}%"),
                User.last_name.ilike(f"%{query}%"),
                TeacherProfile.bio.ilike(f"%{query}%"),
                TeacherProfile.specializations.ilike(f"%{query}%")
            )
            conditions.append(search_filter)
        
        if status is not None:
            conditions.append(
                TeacherProfile.status == TeacherStatus(status.value)
            )
        if is_available is not None:
            conditions.append(TeacherProfile.is_available == is_available)
            
        if conditions:
            stmt = stmt.where(and_(*conditions))
            
        # If filtering by category, join with qualifications
        if category_id:
            stmt = (
                stmt.join(
                    User,
                    TeacherProfile.user_id == User.id
                )
                .join(
                    TeacherQualification,
                    User.id == TeacherQualification.user_id
                )
                .where(
                    TeacherQualification.category_id == category_id
                )
            )
            
        stmt = (
            stmt.offset(skip)
            .limit(limit)
            .order_by(TeacherProfile.created_at.desc())
        )
        
        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def get_user_qualifications(
        db: AsyncSession,
        user_id: str
    ) -> List[TeacherQualification]:
        """
        Get all qualifications for a user
        """
        stmt = select(TeacherQualification).where(
            TeacherQualification.user_id == user_id
        ).options(
            selectinload(TeacherQualification.category),
            selectinload(TeacherQualification.certification)
        ).order_by(TeacherQualification.score_percentage.desc())
        
        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def check_teaching_eligibility(
        db: AsyncSession,
        user_id: str
    ) -> dict:
        """
        Check if user is eligible to become a teacher
        Based on:
        1. User must have 90%+ score qualifications on our certifications
        2. Must apply to teach specific subjects with certifications 
        3. Admin must approve them for those subjects
        4. User remains a student but can teach approved subjects
        """
        # Get user's qualifications (90%+ scores on our certifications)
        qualifications = await TeacherService.get_user_qualifications(
            db, user_id
        )
        
        # Get teacher profile to check application status
        teacher_profile = await TeacherService.get_teacher_profile(db, user_id)
        
        # Group qualifications by category/subject for eligibility breakdown
        qualifications_by_category = {}
        for qual in qualifications:
            category_name = qual.category.name if qual.category else "Unknown"
            if category_name not in qualifications_by_category:
                qualifications_by_category[category_name] = []
            qualifications_by_category[category_name].append({
                "certification_name": qual.certification.name if qual.certification else "Unknown",
                "certification_slug": qual.certification.slug if qual.certification else "unknown",
                "score_percentage": qual.score_percentage,
                "qualified_at": qual.qualified_at.isoformat() if qual.qualified_at else None
            })

        # Determine overall eligibility
        has_qualifications = len(qualifications) > 0
        has_profile = teacher_profile is not None
        is_approved = teacher_profile and teacher_profile.status == TeacherStatus.APPROVED if teacher_profile else False
        
        # Eligibility requirements
        can_apply = has_qualifications and not has_profile
        can_teach = has_qualifications and is_approved
        
        return {
            "is_eligible_to_apply": can_apply,
            "is_eligible_to_teach": can_teach,
            "qualifications_count": len(qualifications),
            "qualified_subjects": len(qualifications_by_category),
            "has_teacher_profile": has_profile,
            "teacher_status": (
                teacher_profile.status.value
                if teacher_profile else None
            ),
            "profile_created_at": (
                teacher_profile.created_at.isoformat() 
                if teacher_profile and teacher_profile.created_at else None
            ),
            "approved_at": (
                teacher_profile.approved_at.isoformat()
                if teacher_profile and teacher_profile.approved_at else None
            ),
            "qualifications_by_subject": qualifications_by_category,
            "next_steps": TeacherService._get_next_steps(
                has_qualifications, has_profile, teacher_profile
            )
        }

    @staticmethod
    def _get_next_steps(
        has_qualifications: bool,
        has_profile: bool,
        teacher_profile: Optional['TeacherProfile']
    ) -> str:
        """
        Determine what the user should do next in their teaching journey
        """
        if not has_qualifications:
            return (
                "You need to earn 90%+ scores on our certifications "
                "to become eligible to teach those subjects."
            )
        
        if not has_profile:
            return (
                "You can now apply to become a teacher! Submit your "
                "teacher application with your qualifications and "
                "external certifications."
            )
        
        if teacher_profile:
            if teacher_profile.status == TeacherStatus.PENDING:
                return (
                    "Your teacher application is under review. "
                    "An admin will approve or reject your application soon."
                )
            elif teacher_profile.status == TeacherStatus.REJECTED:
                return (
                    "Your previous teacher application was rejected. "
                    "Please review the feedback and reapply if needed."
                )
            elif teacher_profile.status == TeacherStatus.APPROVED:
                return (
                    "Congratulations! You are approved to teach. "
                    "You can now create teaching sessions for your "
                    "qualified subjects."
                )
        
        return "Contact support for assistance with your teaching eligibility."

    @staticmethod
    async def apply_to_teach_subject(
        db: AsyncSession,
        user_id: str,
        certification_id: int
    ) -> TeacherQualification:
        """
        Apply to teach a specific subject (create/update teacher profile 
        and qualification)
        """
        # Check if user has passed the certification with 90%+
        best_attempt_stmt = select(QuizAttempt).where(
            and_(
                QuizAttempt.user_id == user_id,
                QuizAttempt.certification_id == certification_id,
                QuizAttempt.score >= 90
            )
        ).order_by(desc(QuizAttempt.score)).limit(1)
        
        result = await db.execute(best_attempt_stmt)
        best_attempt = result.scalar_one_or_none()
        
        if not best_attempt:
            raise ValueError(
                "You must pass the certification with 90% or higher "
                "to be eligible to teach this subject"
            )
        
        # Check if qualification already exists
        existing_qual_stmt = select(TeacherQualification).where(
            and_(
                TeacherQualification.user_id == user_id,
                TeacherQualification.certification_id == certification_id
            )
        )
        existing_result = await db.execute(existing_qual_stmt)
        existing_qual = existing_result.scalar_one_or_none()
        
        if existing_qual:
            if existing_qual.is_active:
                raise ValueError(
                    "You are already qualified to teach this subject"
                )
            else:
                # Reactivate the qualification
                existing_qual.is_active = True
                await db.commit()
                return existing_qual
        
        # Ensure user has a teacher profile (create if needed)
        teacher_profile = await TeacherService.get_teacher_profile(
            db, user_id
        )
        
        if not teacher_profile:
            # Create basic teacher profile
            from .model import TeacherProfileCreate
            profile_data = TeacherProfileCreate(
                bio="New teacher",
                experience="Subject matter expertise through certification"
            )
            teacher_profile = await TeacherService.create_teacher_profile(
                db, user_id, profile_data
            )
        
        # Get certification details
        cert_stmt = select(Certification).where(
            Certification.id == certification_id
        )
        cert_result = await db.execute(cert_stmt)
        certification = cert_result.scalar_one()
        
        # Create the qualification
        score_percentage = (
            best_attempt.correct_answers / best_attempt.total_questions
        ) * 100
        
        qualification = TeacherQualification(
            user_id=user_id,
            category_id=certification.category_id,
            certification_id=certification_id,
            quiz_attempt_id=best_attempt.id,
            score_percentage=score_percentage,
            is_active=True,
            qualified_at=datetime.utcnow()
        )
        
        db.add(qualification)
        await db.commit()
        await db.refresh(qualification)
        
        return qualification