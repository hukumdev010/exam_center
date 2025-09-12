"""AWS Data Analytics Specialty Certification"""

CERTIFICATION = {
    "name": "AWS Certified Data Analytics - Specialty",
    "description": "Design and implement AWS data analytics services to derive value from data",
    "slug": "aws-data-analytics-specialty",
    "level": "Specialty",
    "duration": 180,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service is best for real-time data streaming?",
        "explanation": "Amazon Kinesis is a platform for streaming data on AWS, offering powerful services to make it easy to load and analyze streaming data, and also providing the ability for you to build custom streaming data applications for specialized needs.",
        "reference": "https://docs.aws.amazon.com/kinesis/",
        "points": 1,
        "answers": [
            {"text": "Amazon Kinesis", "is_correct": True},
            {"text": "Amazon SQS", "is_correct": False},
            {"text": "Amazon S3", "is_correct": False},
            {"text": "Amazon RDS", "is_correct": False}
        ]
    },
    {
        "text": "What is Amazon Redshift primarily used for?",
        "explanation": "Amazon Redshift is a fast, scalable data warehouse that makes it simple and cost-effective to analyze all your data across your data warehouse and data lake.",
        "reference": "https://docs.aws.amazon.com/redshift/",
        "points": 1,
        "answers": [
            {"text": "Data warehousing and analytics", "is_correct": True},
            {"text": "Real-time streaming", "is_correct": False},
            {"text": "Object storage", "is_correct": False},
            {"text": "Content delivery", "is_correct": False}
        ]
    },
    {
        "text": "Which service provides serverless interactive query service for S3?",
        "explanation": "Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.",
        "reference": "https://docs.aws.amazon.com/athena/",
        "points": 1,
        "answers": [
            {"text": "Amazon Athena", "is_correct": True},
            {"text": "Amazon EMR", "is_correct": False},
            {"text": "Amazon Redshift", "is_correct": False},
            {"text": "AWS Glue", "is_correct": False}
        ]
    },
    {
        "text": "What is AWS Glue used for?",
        "explanation": "AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics.",
        "reference": "https://docs.aws.amazon.com/glue/",
        "points": 1,
        "answers": [
            {"text": "ETL (Extract, Transform, Load) operations", "is_correct": True},
            {"text": "Data visualization", "is_correct": False},
            {"text": "Real-time streaming", "is_correct": False},
            {"text": "Machine learning model training", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service provides managed Apache Spark?",
        "explanation": "Amazon EMR is the industry-leading cloud big data platform for petabyte-scale data processing, interactive analytics, and machine learning using open-source frameworks such as Apache Spark, Apache Hive, and Presto.",
        "reference": "https://docs.aws.amazon.com/emr/",
        "points": 1,
        "answers": [
            {"text": "Amazon EMR", "is_correct": True},
            {"text": "AWS Glue", "is_correct": False},
            {"text": "Amazon Athena", "is_correct": False},
            {"text": "Amazon Kinesis", "is_correct": False}
        ]
    }
]
