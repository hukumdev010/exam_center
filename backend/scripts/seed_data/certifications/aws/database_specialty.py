"""AWS Database Specialty Certification"""

CERTIFICATION = {
    "name": "AWS Certified Database - Specialty",
    "description": "Design, deploy, and maintain AWS database solutions",
    "slug": "aws-database-specialty",
    "level": "Specialty",
    "duration": 180,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service provides managed relational databases?",
        "explanation": "Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching and backups.",
        "reference": "https://docs.aws.amazon.com/rds/",
        "points": 1,
        "answers": [
            {"text": "Amazon RDS", "is_correct": True},
            {"text": "Amazon DynamoDB", "is_correct": False},
            {"text": "Amazon ElastiCache", "is_correct": False},
            {"text": "Amazon DocumentDB", "is_correct": False}
        ]
    },
    {
        "text": "What type of database is Amazon DynamoDB?",
        "explanation": "Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications.",
        "reference": "https://docs.aws.amazon.com/dynamodb/",
        "points": 1,
        "answers": [
            {"text": "NoSQL (key-value and document)", "is_correct": True},
            {"text": "Relational", "is_correct": False},
            {"text": "Graph", "is_correct": False},
            {"text": "Time-series", "is_correct": False}
        ]
    },
    {
        "text": "Which service provides managed MongoDB-compatible database?",
        "explanation": "Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads.",
        "reference": "https://docs.aws.amazon.com/documentdb/",
        "points": 1,
        "answers": [
            {"text": "Amazon DocumentDB", "is_correct": True},
            {"text": "Amazon DynamoDB", "is_correct": False},
            {"text": "Amazon RDS", "is_correct": False},
            {"text": "Amazon Neptune", "is_correct": False}
        ]
    },
    {
        "text": "What is Amazon Aurora?",
        "explanation": "Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.",
        "reference": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/",
        "points": 1,
        "answers": [
            {"text": "MySQL and PostgreSQL-compatible cloud-native database", "is_correct": True},
            {"text": "NoSQL database", "is_correct": False},
            {"text": "In-memory cache", "is_correct": False},
            {"text": "Graph database", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service provides managed graph database?",
        "explanation": "Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets.",
        "reference": "https://docs.aws.amazon.com/neptune/",
        "points": 1,
        "answers": [
            {"text": "Amazon Neptune", "is_correct": True},
            {"text": "Amazon DynamoDB", "is_correct": False},
            {"text": "Amazon RDS", "is_correct": False},
            {"text": "Amazon ElastiCache", "is_correct": False}
        ]
    }
]
