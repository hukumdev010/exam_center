"""AWS Solutions Architect Associate Certification"""

CERTIFICATION = {
    "name": "AWS Certified Solutions Architect - Associate",
    "description": "Design and deploy scalable, highly available systems on AWS",
    "slug": "aws-solutions-architect-associate",
    "level": "Associate",
    "duration": 130,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service would you use to implement a serverless web application?",
        "explanation": "AWS Lambda, along with API Gateway and other serverless services, enables you to build serverless web applications without managing servers.",
        "reference": "https://docs.aws.amazon.com/lambda/",
        "points": 1,
        "answers": [
            {"text": "Amazon EC2", "is_correct": False},
            {"text": "AWS Lambda", "is_correct": True},
            {"text": "Amazon ECS", "is_correct": False},
            {"text": "AWS Elastic Beanstalk", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Amazon VPC?",
        "explanation": "Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.",
        "reference": "https://docs.aws.amazon.com/vpc/",
        "points": 1,
        "answers": [
            {"text": "To create isolated network environments in AWS", "is_correct": True},
            {"text": "To manage user permissions", "is_correct": False},
            {"text": "To store files securely", "is_correct": False},
            {"text": "To monitor application performance", "is_correct": False}
        ]
    },
    {
        "text": "Which storage class in Amazon S3 is most cost-effective for long-term archival?",
        "explanation": "S3 Glacier Deep Archive is the lowest-cost storage class for long-term retention and digital preservation for data that may be accessed once or twice in a year.",
        "reference": "https://docs.aws.amazon.com/s3/latest/userguide/storage-class-intro.html",
        "points": 1,
        "answers": [
            {"text": "S3 Standard", "is_correct": False},
            {"text": "S3 Intelligent-Tiering", "is_correct": False},
            {"text": "S3 Glacier", "is_correct": False},
            {"text": "S3 Glacier Deep Archive", "is_correct": True}
        ]
    }
]
