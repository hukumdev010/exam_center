from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    Float,
    Enum,
    Table,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

Base = declarative_base()


# RBAC Association Tables
user_roles = Table(
    'user_roles',
    Base.metadata,
    Column(
        'user_id',
        String,
        ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True
    ),
    Column(
        'role_id',
        Integer,
        ForeignKey(
            'roles.id',
            ondelete='CASCADE'
        ),
        primary_key=True
    ),
    Column('assigned_at', DateTime, default=func.now()),
    Column(
        'assigned_by',
        String,
        ForeignKey('users.id', name='fk_user_roles_assigned_by'),
        nullable=True
    )
)

role_policies = Table(
    'role_policies',
    Base.metadata,
    Column(
        'role_id',
        Integer,
        ForeignKey('roles.id', ondelete='CASCADE'),
        primary_key=True
    ),
    Column('policy_id', Integer, ForeignKey('policies.id', ondelete='CASCADE'), primary_key=True),
    Column('created_at', DateTime, default=func.now())
)

role_permissions = Table(
    'role_permissions',
    Base.metadata,
    Column(
        'role_id',
        Integer,
        ForeignKey('roles.id', ondelete='CASCADE'),
        primary_key=True
    ),
    Column(
        'permission_id',
        Integer,
        ForeignKey('permissions.id', ondelete='CASCADE'),
        primary_key=True
    ),
    Column('created_at', DateTime, default=func.now())
)

permission_policies = Table(
    'permission_policies',
    Base.metadata,
    Column('permission_id', Integer, ForeignKey('permissions.id', ondelete='CASCADE'), primary_key=True),
    Column('policy_id', Integer, ForeignKey('policies.id', ondelete='CASCADE'), primary_key=True),
    Column('created_at', DateTime, default=func.now())
)


# RBAC Models

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # e.g., "readCategory", "updateCategory"
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    # e.g., "category", "certification", "user"
    resource = Column(String, nullable=False)
    # e.g., "read", "create", "update", "delete"
    action = Column(String, nullable=False)
    # System policies cannot be deleted
    is_system = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    roles = relationship(
        "Role", secondary=role_policies, back_populates="policies"
    )
    permissions = relationship(
        "Permission",
        secondary=permission_policies,
        back_populates="policies"
    )


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # e.g., "CategoryManager", "StudentAccess"
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    # System permissions cannot be deleted
    is_system = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    roles = relationship(
        "Role", secondary=role_permissions, back_populates="permissions"
    )
    policies = relationship(
        "Policy", secondary=permission_policies, back_populates="permissions"
    )


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # e.g., "student", "teacher", "admin", "superadmin"
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    # System roles cannot be deleted
    is_system = Column(Boolean, default=False)
    # Default role assigned to new users
    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    users = relationship(
        "User", 
        secondary=user_roles, 
        back_populates="roles",
        primaryjoin="Role.id == user_roles.c.role_id",
        secondaryjoin="User.id == user_roles.c.user_id"
    )
    policies = relationship(
        "Policy", 
        secondary=role_policies, 
        back_populates="roles"
    )
    permissions = relationship(
        "Permission", 
        secondary=role_permissions, 
        back_populates="roles"
    )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=False)
    icon = Column(String, nullable=True)  # Icon name for UI
    color = Column(String, nullable=True)  # Color theme for UI
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    parent = relationship(
        "Category", remote_side=[id], back_populates="children"
    )
    children = relationship("Category", back_populates="parent")
    certifications = relationship("Certification", back_populates="category")


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=False)
    # Associate, Professional, Specialty, etc.
    level = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)  # Exam duration in minutes
    # Number of questions in the exam
    questions_count = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Quiz benefits and advantages
    benefits = Column(Text, nullable=True)  # JSON or text benefits
    advantages = Column(Text, nullable=True)  # JSON or text advantages
    career_benefits = Column(Text, nullable=True)  # Career benefits
    teaching_eligibility = Column(Boolean, default=False)  # Teacher eligible
    min_score_for_teaching = Column(Integer, default=90)  # Min teaching score
    min_score_for_certificate = Column(Integer, default=80)  # Min cert score
    
    # Syllabus and curriculum information
    syllabus = Column(Text, nullable=True)  # Structured syllabus content (JSON)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    category = relationship("Category", back_populates="certifications")
    questions = relationship("Question", back_populates="certification")
    user_progress = relationship(
        "UserProgress",
        back_populates="certification")
    quiz_attempts = relationship("QuizAttempt", back_populates="certification")
    syllabus_modules = relationship(
        "SyllabusModule",
        back_populates="certification",
        cascade="all, delete-orphan",
        order_by="SyllabusModule.order_index"
    )


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    explanation = Column(String, nullable=True)
    # URL reference for additional information
    reference = Column(String, nullable=True)
    points = Column(Integer, default=1)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    certification = relationship("Certification", back_populates="questions")
    answers = relationship(
        "Answer", back_populates="question", cascade="all, delete-orphan"
    )
    ai_assistant = relationship(
        "QuestionAIAssistant", 
        back_populates="question", 
        cascade="all, delete-orphan"
    )


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(
        Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    question = relationship("Question", back_populates="answers")


class QuestionAIAssistant(Base):
    __tablename__ = "question_ai_assistant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(
        Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False
    )
    # Hash of the question content to detect changes
    question_hash = Column(String, nullable=False)
    # AI assistant response content
    ai_response = Column(Text, nullable=False)
    # Model used for generation (e.g., "gemini-2.5-flash")
    model_name = Column(String, default="gemini-2.5-flash")
    # Token count for cost tracking
    token_count = Column(Integer, nullable=True)
    # Cache hit count for analytics
    cache_hits = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    question = relationship("Question", back_populates="ai_assistant")

    __table_args__ = (UniqueConstraint("question_id", "question_hash"),)


# NextAuth.js Models


class Account(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    type = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    provider_account_id = Column(String, nullable=False)
    refresh_token = Column(Text, nullable=True)
    access_token = Column(Text, nullable=True)
    expires_at = Column(Integer, nullable=True)
    token_type = Column(String, nullable=True)
    scope = Column(String, nullable=True)
    id_token = Column(Text, nullable=True)
    session_state = Column(String, nullable=True)

    # Relationships
    user = relationship("User", back_populates="accounts")

    __table_args__ = (UniqueConstraint("provider", "provider_account_id"),)


class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True)
    session_token = Column(String, unique=True, nullable=False)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    expires = Column(DateTime, nullable=False)

    # Relationships
    user = relationship("User", back_populates="sessions")


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    email_verified = Column(DateTime, nullable=True)
    image = Column(String, nullable=True)
    password_hash = Column(String, nullable=True)  # For email/password authentication
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    accounts = relationship(
        "Account", back_populates="user", cascade="all, delete-orphan"
    )
    sessions = relationship(
        "Session", back_populates="user", cascade="all, delete-orphan"
    )
    progress = relationship(
        "UserProgress", back_populates="user", cascade="all, delete-orphan"
    )
    quiz_attempts = relationship(
        "QuizAttempt", back_populates="user", cascade="all, delete-orphan"
    )
    # RBAC relationships
    roles = relationship(
        "Role", 
        secondary=user_roles, 
        back_populates="users",
        primaryjoin="User.id == user_roles.c.user_id",
        secondaryjoin="Role.id == user_roles.c.role_id"
    )

    # Teacher-Student system relationships
    teacher_qualifications = relationship(
        "TeacherQualification",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    teacher_profile = relationship(
        "TeacherProfile",
        back_populates="user",
        cascade="all, delete-orphan",
        foreign_keys="TeacherProfile.user_id"
    )
    session_bookings = relationship(
        "SessionBooking",
        back_populates="student",
        cascade="all, delete-orphan"
    )
    certificates = relationship(
        "Certificate",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class VerificationToken(Base):
    __tablename__ = "verification_tokens"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    expires = Column(DateTime, nullable=False)

    __table_args__ = (UniqueConstraint("identifier", "token"),)


# User Progress Tracking


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False)
    current_question = Column(Integer, default=0)
    total_questions = Column(Integer, nullable=False)
    correct_answers = Column(Integer, default=0)
    points = Column(Integer, default=0)
    is_completed = Column(Boolean, default=False)
    last_active_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="progress")
    certification = relationship(
        "Certification",
        back_populates="user_progress")

    __table_args__ = (UniqueConstraint("user_id", "certification_id"),)


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False)
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    correct_answers = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    completed_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())

    # Relationships
    user = relationship("User", back_populates="quiz_attempts")
    certification = relationship(
        "Certification",
        back_populates="quiz_attempts")


# Teacher-Student System Enums
class TeacherStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    SUSPENDED = "suspended"


class SessionType(enum.Enum):
    ONE_ON_ONE = "one_on_one"
    GROUP = "group"


class SessionStatus(enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"


class BookingStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


# Teacher Qualification Model
class TeacherQualification(Base):
    __tablename__ = "teacher_qualifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False
    )
    quiz_attempt_id = Column(
        String,
        ForeignKey("quiz_attempts.id"),
        nullable=False
    )
    score_percentage = Column(Float, nullable=False)  # The 90%+ score
    is_active = Column(Boolean, default=True)
    qualified_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="teacher_qualifications")
    category = relationship("Category")
    certification = relationship("Certification")
    quiz_attempt = relationship("QuizAttempt")
    
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "certification_id",
            name="unique_user_certification_qualification"
        ),
    )


# Teacher Profile Model
class TeacherProfile(Base):
    __tablename__ = "teacher_profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    bio = Column(Text, nullable=True)
    qualifications = Column(Text, nullable=True)  # Educational qualifications
    experience = Column(Text, nullable=True)  # Professional experience
    github_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    website_url = Column(String, nullable=True)
    experience_years = Column(Integer, nullable=True)
    hourly_rate_one_on_one = Column(Float, nullable=True)  # USD per hour 1:1
    hourly_rate_group = Column(Float, nullable=True)  # USD/hour/student group
    max_group_size = Column(Integer, default=10)
    status = Column(Enum(TeacherStatus), default=TeacherStatus.PENDING)
    is_available = Column(Boolean, default=True)
    languages_spoken = Column(String, nullable=True)  # JSON array as string
    timezone = Column(String, nullable=True)
    admin_notes = Column(Text, nullable=True)  # Admin approval notes
    approved_by = Column(String, ForeignKey("users.id"), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    rejection_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship(
        "User",
        back_populates="teacher_profile",
        foreign_keys=[user_id]
    )
    approved_by_user = relationship(
        "User",
        foreign_keys=[approved_by]
    )
    sessions = relationship("TeachingSession", back_populates="teacher")
    

# Teaching Session Model (for both one-on-one and group sessions)
class TeachingSession(Base):
    __tablename__ = "teaching_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(
        Integer,
        ForeignKey("teacher_profiles.id", ondelete="CASCADE"),
        nullable=False
    )
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=True  # Can be general category teaching
    )
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    session_type = Column(Enum(SessionType), nullable=False)
    max_participants = Column(Integer, nullable=False, default=1)  # 1:1 or >1
    current_participants = Column(Integer, default=0)
    duration_minutes = Column(Integer, nullable=False)  # Session duration
    price_per_participant = Column(Float, nullable=False)  # Price per student
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.SCHEDULED)
    meeting_link = Column(String, nullable=True)  # Zoom, Google Meet, etc.
    meeting_password = Column(String, nullable=True)
    notes = Column(Text, nullable=True)  # Teacher's notes for the session
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    teacher = relationship("TeacherProfile", back_populates="sessions")
    category = relationship("Category")
    certification = relationship("Certification")
    bookings = relationship(
        "SessionBooking",
        back_populates="session",
        cascade="all, delete-orphan"
    )


# Session Booking Model
class SessionBooking(Base):
    __tablename__ = "session_bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(
        Integer,
        ForeignKey("teaching_sessions.id", ondelete="CASCADE"),
        nullable=False
    )
    student_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    status = Column(Enum(BookingStatus), default=BookingStatus.PENDING)
    amount_paid = Column(Float, nullable=False)
    payment_method = Column(String, nullable=True)  # stripe, paypal, etc.
    payment_transaction_id = Column(String, nullable=True)
    booking_notes = Column(Text, nullable=True)  # Student's notes/questions
    attendance_confirmed = Column(Boolean, default=False)
    feedback_rating = Column(Integer, nullable=True)  # 1-5 stars
    feedback_comment = Column(Text, nullable=True)
    booked_at = Column(DateTime, default=func.now())
    cancelled_at = Column(DateTime, nullable=True)
    cancellation_reason = Column(Text, nullable=True)

    # Relationships
    session = relationship("TeachingSession", back_populates="bookings")
    student = relationship("User", back_populates="session_bookings")


# Certificate Model
class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    quiz_attempt_id = Column(
        String,
        ForeignKey("quiz_attempts.id", ondelete="CASCADE"),
        nullable=False,
        unique=True  # One certificate per quiz attempt
    )
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False
    )
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    pdf_filename = Column(String, nullable=True)  # Stored PDF filename
    issued_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())

    # Relationships
    user = relationship("User", back_populates="certificates")
    quiz_attempt = relationship("QuizAttempt")
    certification = relationship("Certification")


# Syllabus Content Models
class SyllabusModule(Base):
    __tablename__ = "syllabus_modules"

    id = Column(Integer, primary_key=True, autoincrement=True)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id", ondelete="CASCADE"),
        nullable=False
    )
    module_number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    duration = Column(String, nullable=True)  # e.g., "Week 1", "2 hours"
    order_index = Column(Integer, nullable=False)  # For ordering modules
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    certification = relationship("Certification", back_populates="syllabus_modules")
    topics = relationship(
        "SyllabusTopic", 
        back_populates="module",
        cascade="all, delete-orphan",
        order_by="SyllabusTopic.order_index"
    )
    learning_objectives = relationship(
        "ModuleLearningObjective",
        back_populates="module",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("certification_id", "module_number"),
        UniqueConstraint("certification_id", "order_index")
    )


class SyllabusTopic(Base):
    __tablename__ = "syllabus_topics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(
        Integer,
        ForeignKey("syllabus_modules.id", ondelete="CASCADE"),
        nullable=False
    )
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    introduction = Column(Text, nullable=True)
    order_index = Column(Integer, nullable=False)
    estimated_duration = Column(String, nullable=True)  # e.g., "30 minutes"
    is_active = Column(Boolean, default=True)
    
    # Content for creating YouTube videos
    video_script_outline = Column(Text, nullable=True)  # What to teach in video
    practical_examples = Column(Text, nullable=True)  # JSON array of examples
    key_points = Column(Text, nullable=True)  # JSON array of key points
    
    # Video content when available
    video_url = Column(String, nullable=True)  # YouTube URL
    video_duration = Column(Integer, nullable=True)  # Duration in seconds
    video_status = Column(String, default="planned")  # planned, scripted, recorded, published
    
    # Detailed comprehensive content (JSON format)
    detailed_content = Column(Text, nullable=True)  # JSON content
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    module = relationship("SyllabusModule", back_populates="topics")
    content_sections = relationship(
        "TopicContentSection",
        back_populates="topic",
        cascade="all, delete-orphan",
        order_by="TopicContentSection.order_index"
    )

    __table_args__ = (
        UniqueConstraint("module_id", "order_index"),
    )


class TopicContentSection(Base):
    __tablename__ = "topic_content_sections"

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_id = Column(
        Integer,
        ForeignKey("syllabus_topics.id", ondelete="CASCADE"),
        nullable=False
    )
    section_type = Column(String, nullable=False)  # introduction, key_points, examples, what_to_teach, etc.
    title = Column(String, nullable=True)
    content = Column(Text, nullable=False)  # The actual content
    order_index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    topic = relationship("SyllabusTopic", back_populates="content_sections")

    __table_args__ = (
        UniqueConstraint("topic_id", "order_index"),
    )


class ModuleLearningObjective(Base):
    __tablename__ = "module_learning_objectives"

    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(
        Integer,
        ForeignKey("syllabus_modules.id", ondelete="CASCADE"),
        nullable=False
    )
    objective = Column(String, nullable=False)
    order_index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    # Relationships
    module = relationship("SyllabusModule", back_populates="learning_objectives")

    __table_args__ = (
        UniqueConstraint("module_id", "order_index"),
    )
