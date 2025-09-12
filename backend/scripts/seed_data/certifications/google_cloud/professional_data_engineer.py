"""Google Cloud Professional Data Engineer Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional Data Engineer",
    "description": "Design, build, operationalize, secure, and monitor data processing systems on Google Cloud",
    "slug": "google-professional-data-engineer",
    "level": "Professional",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "google-cloud",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service is best for real-time stream processing?",
        "explanation": "Cloud Dataflow is a fully managed service for stream and batch processing that can handle real-time data streams with low latency.",
        "reference": "https://cloud.google.com/dataflow/docs",
        "points": 1,
        "answers": [
            {"text": "BigQuery", "is_correct": False},
            {"text": "Cloud Dataflow", "is_correct": True},
            {"text": "Cloud Storage", "is_correct": False},
            {"text": "Cloud Pub/Sub", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary purpose of Cloud Pub/Sub?",
        "explanation": "Cloud Pub/Sub is a messaging service that allows applications to send and receive messages between independent applications, enabling event-driven architectures.",
        "reference": "https://cloud.google.com/pubsub/docs",
        "points": 1,
        "answers": [
            {"text": "Data warehousing", "is_correct": False},
            {"text": "Messaging and event ingestion", "is_correct": True},
            {"text": "Machine learning", "is_correct": False},
            {"text": "File storage", "is_correct": False}
        ]
    },
    {
        "text": "Which Google Cloud service provides a managed Apache Spark and Hadoop environment?",
        "explanation": "Cloud Dataproc is a managed service that provides Apache Spark, Hadoop, and other big data tools in a fully managed environment.",
        "reference": "https://cloud.google.com/dataproc/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Dataproc", "is_correct": True},
            {"text": "Cloud Dataflow", "is_correct": False},
            {"text": "BigQuery", "is_correct": False},
            {"text": "Cloud Composer", "is_correct": False}
        ]
    },
    {
        "text": "What is the recommended approach for data transformation in BigQuery?",
        "explanation": "SQL is the primary and recommended approach for data transformation in BigQuery, with support for complex analytics functions and user-defined functions.",
        "reference": "https://cloud.google.com/bigquery/docs/data-transformation",
        "points": 1,
        "answers": [
            {"text": "Python scripts", "is_correct": False},
            {"text": "SQL transformations", "is_correct": True},
            {"text": "Java applications", "is_correct": False},
            {"text": "REST APIs", "is_correct": False}
        ]
    },
    {
        "text": "Which Google Cloud service orchestrates and schedules data workflows?",
        "explanation": "Cloud Composer is a managed Apache Airflow service that orchestrates workflows spanning multiple clouds and on-premises data centers.",
        "reference": "https://cloud.google.com/composer/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Scheduler", "is_correct": False},
            {"text": "Cloud Composer", "is_correct": True},
            {"text": "Cloud Functions", "is_correct": False},
            {"text": "Cloud Build", "is_correct": False}
        ]
    }
]
