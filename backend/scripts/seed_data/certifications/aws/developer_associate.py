"""AWS Developer Associate Certification"""

CERTIFICATION = {
    "name": "AWS Certified Developer - Associate",
    "description": "Develop and maintain applications on AWS",
    "slug": "aws-developer-associate",
    "level": "Associate",
    "duration": 130,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service is best suited for implementing a message queue?",
        "explanation": "Amazon SQS (Simple Queue Service) is a fully managed message queuing service that enables you to decouple and scale microservices.",
        "reference": "https://docs.aws.amazon.com/sqs/",
        "points": 1,
        "answers": [
            {"text": "Amazon SNS", "is_correct": False},
            {"text": "Amazon SQS", "is_correct": True},
            {"text": "AWS Lambda", "is_correct": False},
            {"text": "Amazon EventBridge", "is_correct": False}
        ]
    }
]
