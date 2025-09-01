import asyncio
import sys
import os
from datetime import datetime
from uuid import uuid4

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import engine, AsyncSessionLocal
from models import Base, Category, Certification, Question, Answer

async def seed_database():
    """Seed the database with sample data"""
    print("🌱 Starting database seeding...")
    
    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created")
    
    async with AsyncSessionLocal() as session:
        try:
            # Create categories
            aws_category = Category(
                name="AWS",
                description="Amazon Web Services Certifications",
                slug="aws",
                icon="aws",
                color="orange"
            )
            
            devops_category = Category(
                name="DevOps",
                description="DevOps and Infrastructure Certifications",
                slug="devops",
                icon="devops",
                color="blue"
            )
            
            programming_category = Category(
                name="Programming",
                description="Programming Languages and Frameworks",
                slug="programming",
                icon="code",
                color="green"
            )
            
            session.add_all([aws_category, devops_category, programming_category])
            await session.flush()  # To get IDs
            
            # Create certifications
            aws_saa = Certification(
                name="AWS Solutions Architect Associate",
                description="Design distributed systems on AWS",
                slug="aws-solutions-architect-associate",
                level="Associate",
                duration=130,
                questions_count=10,  # Sample size
                category_id=aws_category.id,
                is_active=True
            )
            
            docker_cert = Certification(
                name="Docker Certified Associate",
                description="Docker containerization certification",
                slug="docker-certified-associate",
                level="Associate",
                duration=90,
                questions_count=5,  # Sample size
                category_id=devops_category.id,
                is_active=True
            )
            
            python_cert = Certification(
                name="Python Programming",
                description="Python programming fundamentals",
                slug="python-programming",
                level="Beginner",
                duration=60,
                questions_count=8,  # Sample size
                category_id=programming_category.id,
                is_active=True
            )
            
            session.add_all([aws_saa, docker_cert, python_cert])
            await session.flush()  # To get IDs
            
            # Add sample questions for AWS SAA
            aws_questions = [
                {
                    "text": "Which AWS service provides a fully managed NoSQL database?",
                    "explanation": "Amazon DynamoDB is AWS's fully managed NoSQL database service.",
                    "reference": "https://docs.aws.amazon.com/dynamodb/",
                    "answers": [
                        {"text": "Amazon RDS", "is_correct": False},
                        {"text": "Amazon DynamoDB", "is_correct": True},
                        {"text": "Amazon Redshift", "is_correct": False},
                        {"text": "Amazon Aurora", "is_correct": False}
                    ]
                },
                {
                    "text": "What is the maximum size of an S3 object?",
                    "explanation": "The maximum size of a single S3 object is 5 TB.",
                    "reference": "https://docs.aws.amazon.com/s3/",
                    "answers": [
                        {"text": "5 GB", "is_correct": False},
                        {"text": "5 TB", "is_correct": True},
                        {"text": "1 TB", "is_correct": False},
                        {"text": "100 GB", "is_correct": False}
                    ]
                }
            ]
            
            # Add sample questions for Docker
            docker_questions = [
                {
                    "text": "What command is used to build a Docker image?",
                    "explanation": "The 'docker build' command creates a Docker image from a Dockerfile.",
                    "reference": "https://docs.docker.com/engine/reference/commandline/build/",
                    "answers": [
                        {"text": "docker create", "is_correct": False},
                        {"text": "docker build", "is_correct": True},
                        {"text": "docker make", "is_correct": False},
                        {"text": "docker compile", "is_correct": False}
                    ]
                }
            ]
            
            # Add sample questions for Python
            python_questions = [
                {
                    "text": "Which of the following is a mutable data type in Python?",
                    "explanation": "Lists are mutable in Python, meaning their contents can be changed.",
                    "reference": "https://docs.python.org/3/tutorial/datastructures.html",
                    "answers": [
                        {"text": "tuple", "is_correct": False},
                        {"text": "string", "is_correct": False},
                        {"text": "list", "is_correct": True},
                        {"text": "frozenset", "is_correct": False}
                    ]
                }
            ]
            
            # Create questions and answers
            for question_data in aws_questions:
                question = Question(
                    text=question_data["text"],
                    explanation=question_data["explanation"],
                    reference=question_data["reference"],
                    points=1,
                    certification_id=aws_saa.id
                )
                session.add(question)
                await session.flush()  # To get question ID
                
                for answer_data in question_data["answers"]:
                    answer = Answer(
                        text=answer_data["text"],
                        is_correct=answer_data["is_correct"],
                        question_id=question.id
                    )
                    session.add(answer)
            
            for question_data in docker_questions:
                question = Question(
                    text=question_data["text"],
                    explanation=question_data["explanation"],
                    reference=question_data["reference"],
                    points=1,
                    certification_id=docker_cert.id
                )
                session.add(question)
                await session.flush()
                
                for answer_data in question_data["answers"]:
                    answer = Answer(
                        text=answer_data["text"],
                        is_correct=answer_data["is_correct"],
                        question_id=question.id
                    )
                    session.add(answer)
            
            for question_data in python_questions:
                question = Question(
                    text=question_data["text"],
                    explanation=question_data["explanation"],
                    reference=question_data["reference"],
                    points=1,
                    certification_id=python_cert.id
                )
                session.add(question)
                await session.flush()
                
                for answer_data in question_data["answers"]:
                    answer = Answer(
                        text=answer_data["text"],
                        is_correct=answer_data["is_correct"],
                        question_id=question.id
                    )
                    session.add(answer)
            
            await session.commit()
            print("✅ Database seeded successfully!")
            
        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            await session.rollback()
            raise

if __name__ == "__main__":
    asyncio.run(seed_database())
