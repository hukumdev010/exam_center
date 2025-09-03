"""AWS Solutions Architect Professional Certification"""

CERTIFICATION = {
    "name": "AWS Certified Solutions Architect - Professional",
    "description": "Advanced architectural knowledge for complex AWS solutions",
    "slug": "aws-solutions-architect-professional",
    "level": "Professional",
    "duration": 180,
    "questions_count": 75,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service provides automated backup and disaster recovery for on-premises workloads?",
        "explanation": "AWS DataSync with AWS Storage Gateway provides comprehensive backup and disaster recovery solutions for hybrid architectures.",
        "reference": "https://docs.aws.amazon.com/datasync/",
        "points": 1,
        "answers": [
            {"text": "AWS DataSync", "is_correct": True},
            {"text": "AWS Direct Connect", "is_correct": False},
            {"text": "AWS Site-to-Site VPN", "is_correct": False},
            {"text": "AWS Transit Gateway", "is_correct": False}
        ]
    }
]
