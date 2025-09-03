"""AWS Security Specialty Certification"""

CERTIFICATION = {
    "name": "AWS Certified Security - Specialty",
    "description": "Specialized knowledge in AWS security",
    "slug": "aws-security-specialty",
    "level": "Specialty",
    "duration": 170,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service provides centralized logging for security analysis?",
        "explanation": "AWS CloudTrail provides event history of AWS API calls, which is essential for security analysis and compliance.",
        "reference": "https://docs.aws.amazon.com/cloudtrail/",
        "points": 1,
        "answers": [
            {"text": "AWS Config", "is_correct": False},
            {"text": "AWS CloudTrail", "is_correct": True},
            {"text": "Amazon CloudWatch", "is_correct": False},
            {"text": "AWS Systems Manager", "is_correct": False}
        ]
    }
]
