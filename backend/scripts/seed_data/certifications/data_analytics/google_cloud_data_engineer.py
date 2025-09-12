"""Google Cloud Professional Data Engineer Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional Data Engineer",
    "description": "Design and build data processing systems and machine learning models on Google Cloud Platform",
    "slug": "google-cloud-professional-data-engineer",
    "level": "Professional",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "data-analytics",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service is best for real-time stream processing?",
        "explanation": "Cloud Dataflow is Google Cloud's fully managed service for stream and batch data processing, based on Apache Beam, providing real-time data processing capabilities.",
        "reference": "https://cloud.google.com/dataflow/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Dataflow", "is_correct": True},
            {"text": "BigQuery", "is_correct": False},
            {"text": "Cloud Storage", "is_correct": False},
            {"text": "Cloud SQL", "is_correct": False}
        ]
    },
    {
        "text": "What is BigQuery's primary use case?",
        "explanation": "BigQuery is Google Cloud's serverless, highly scalable data warehouse designed for analyzing large datasets using SQL queries with massive parallel processing capabilities.",
        "reference": "https://cloud.google.com/bigquery/docs",
        "points": 1,
        "answers": [
            {"text": "Serverless data warehouse for analytics", "is_correct": True},
            {"text": "Real-time messaging", "is_correct": False},
            {"text": "File storage", "is_correct": False},
            {"text": "Machine learning training", "is_correct": False}
        ]
    },
    {
        "text": "Which service provides managed Apache Spark on Google Cloud?",
        "explanation": "Cloud Dataproc is Google Cloud's managed Apache Spark and Hadoop service that allows you to run big data workloads in a fully managed environment.",
        "reference": "https://cloud.google.com/dataproc/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Dataproc", "is_correct": True},
            {"text": "Cloud Dataflow", "is_correct": False},
            {"text": "Cloud Composer", "is_correct": False},
            {"text": "Cloud Functions", "is_correct": False}
        ]
    },
    {
        "text": "What is Cloud Pub/Sub used for?",
        "explanation": "Cloud Pub/Sub is a messaging service that enables asynchronous communication between applications, supporting real-time event-driven architectures and data ingestion pipelines.",
        "reference": "https://cloud.google.com/pubsub/docs",
        "points": 1,
        "answers": [
            {"text": "Asynchronous messaging and event streaming", "is_correct": True},
            {"text": "Data warehouse storage", "is_correct": False},
            {"text": "Machine learning model training", "is_correct": False},
            {"text": "User authentication", "is_correct": False}
        ]
    },
    {
        "text": "Which tool is used for data pipeline orchestration on Google Cloud?",
        "explanation": "Cloud Composer is Google Cloud's managed Apache Airflow service that provides workflow orchestration for data pipelines and ETL processes.",
        "reference": "https://cloud.google.com/composer/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Composer", "is_correct": True},
            {"text": "Cloud Scheduler", "is_correct": False},
            {"text": "Cloud Tasks", "is_correct": False},
            {"text": "Cloud Build", "is_correct": False}
        ]
    }
]
