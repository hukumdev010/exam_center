import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=False)
    icon = Column(String, nullable=True)  # Icon name for UI
    color = Column(String, nullable=True)  # Color theme for UI
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    certifications = relationship("Certification", back_populates="category")

class Certification(Base):
    __tablename__ = "certifications"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=False)
    level = Column(String, nullable=True)  # Associate, Professional, Specialty, etc.
    duration = Column(Integer, nullable=True)  # Exam duration in minutes
    questions_count = Column(Integer, nullable=True)  # Number of questions in the exam
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    category = relationship("Category", back_populates="certifications")
    questions = relationship("Question", back_populates="certification")
    user_progress = relationship("UserProgress", back_populates="certification")
    quiz_attempts = relationship("QuizAttempt", back_populates="certification")

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    explanation = Column(String, nullable=True)
    reference = Column(String, nullable=True)  # URL reference for additional information
    points = Column(Integer, default=1)
    certification_id = Column(Integer, ForeignKey("certifications.id"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    certification = relationship("Certification", back_populates="questions")
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    question = relationship("Question", back_populates="answers")

# NextAuth.js Models
class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
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
    
    __table_args__ = (
        UniqueConstraint('provider', 'provider_account_id'),
    )

class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(String, primary_key=True)
    session_token = Column(String, unique=True, nullable=False)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
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
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    accounts = relationship("Account", back_populates="user", cascade="all, delete-orphan")
    sessions = relationship("Session", back_populates="user", cascade="all, delete-orphan")
    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
    quiz_attempts = relationship("QuizAttempt", back_populates="user", cascade="all, delete-orphan")

class VerificationToken(Base):
    __tablename__ = "verification_tokens"
    
    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    expires = Column(DateTime, nullable=False)
    
    __table_args__ = (
        UniqueConstraint('identifier', 'token'),
    )

# User Progress Tracking
class UserProgress(Base):
    __tablename__ = "user_progress"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    certification_id = Column(Integer, ForeignKey("certifications.id"), nullable=False)
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
    certification = relationship("Certification", back_populates="user_progress")
    
    __table_args__ = (
        UniqueConstraint('user_id', 'certification_id'),
    )

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    certification_id = Column(Integer, ForeignKey("certifications.id"), nullable=False)
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    correct_answers = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    completed_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="quiz_attempts")
    certification = relationship("Certification", back_populates="quiz_attempts")
