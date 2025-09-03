"""AWS Cloud Practitioner Certification"""

CERTIFICATION = {
    "name": "AWS Certified Cloud Practitioner",
    "description": "Foundational understanding of AWS Cloud",
    "slug": "aws-cloud-practitioner",
    "level": "Foundational",
    "duration": 90,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the AWS Well-Architected Framework?",
        "explanation": "The AWS Well-Architected Framework provides guidance to help customers build secure, high-performing, resilient, and efficient infrastructure for their applications.",
        "reference": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
        "points": 1,
        "answers": [
            {"text": "A set of best practices for building on AWS", "is_correct": True},
            {"text": "A billing calculation tool", "is_correct": False},
            {"text": "A monitoring service", "is_correct": False},
            {"text": "A deployment automation tool", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service provides a fully managed NoSQL database?",
        "explanation": "Amazon DynamoDB is AWS's fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.",
        "reference": "https://docs.aws.amazon.com/dynamodb/",
        "points": 1,
        "answers": [
            {"text": "Amazon RDS", "is_correct": False},
            {"text": "Amazon DynamoDB", "is_correct": True},
            {"text": "Amazon Redshift", "is_correct": False},
            {"text": "Amazon Aurora", "is_correct": False}
        ]
    },
    {
        "text": "What is the maximum size of a single object that can be stored in Amazon S3?",
        "explanation": "The maximum size of a single S3 object is 5 TB (terabytes).",
        "reference": "https://docs.aws.amazon.com/s3/",
        "points": 1,
        "answers": [
            {"text": "5 GB", "is_correct": False},
            {"text": "5 TB", "is_correct": True},
            {"text": "1 TB", "is_correct": False},
            {"text": "100 GB", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service is used for content delivery and caching?",
        "explanation": "Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally.",
        "reference": "https://docs.aws.amazon.com/cloudfront/",
        "points": 1,
        "answers": [
            {"text": "Amazon Route 53", "is_correct": False},
            {"text": "Amazon CloudFront", "is_correct": True},
            {"text": "AWS Global Accelerator", "is_correct": False},
            {"text": "Amazon API Gateway", "is_correct": False}
        ]
    },
    {
        "text": "What does AWS IAM stand for?",
        "explanation": "AWS IAM stands for Identity and Access Management, which enables you to manage access to AWS services and resources securely.",
        "reference": "https://docs.aws.amazon.com/iam/",
        "points": 1,
        "answers": [
            {"text": "Internet Access Management", "is_correct": False},
            {"text": "Identity and Access Management", "is_correct": True},
            {"text": "Infrastructure Application Management", "is_correct": False},
            {"text": "Internal Account Management", "is_correct": False}
        ]
    }
]
