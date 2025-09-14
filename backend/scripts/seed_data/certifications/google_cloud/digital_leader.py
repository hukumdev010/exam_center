"""Google Cloud Digital Leader Certification"""

CERTIFICATION = {
    "name": "Google Cloud Digital Leader",
    "description": "Foundational knowledge of Google Cloud",
    "slug": "google-cloud-digital-leader",
    "level": "Foundational",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "google-cloud",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Google Cloud Platform (GCP)?",
        "explanation": "Google Cloud Platform is a suite of cloud computing services that provides infrastructure, platform, and software services for building, deploying, and scaling applications on Google's infrastructure.",
        "reference": "https://cloud.google.com/docs/overview",
        "points": 1,
        "answers": [
            {"text": "A web browser", "is_correct": False},
            {"text": "A cloud computing platform", "is_correct": True},
            {"text": "A programming language", "is_correct": False},
            {"text": "A database system", "is_correct": False},
        ],
    },
    {
        "text": "Which Google Cloud service is used for virtual machine instances?",
        "explanation": "Google Compute Engine provides scalable virtual machine instances running in Google's data centers. It offers both predefined and custom machine types.",
        "reference": "https://cloud.google.com/compute",
        "points": 1,
        "answers": [
            {"text": "Google App Engine", "is_correct": False},
            {"text": "Google Compute Engine", "is_correct": True},
            {"text": "Google Cloud Functions", "is_correct": False},
            {"text": "Google Kubernetes Engine", "is_correct": False},
        ],
    },
    {
        "text": "What is BigQuery in Google Cloud?",
        "explanation": "BigQuery is Google Cloud's fully managed, serverless data warehouse that enables super-fast SQL queries using the processing power of Google's infrastructure.",
        "reference": "https://cloud.google.com/bigquery",
        "points": 1,
        "answers": [
            {"text": "A virtual machine service", "is_correct": False},
            {"text": "A serverless data warehouse for analytics", "is_correct": True},
            {"text": "A container orchestration platform", "is_correct": False},
            {"text": "A file storage service", "is_correct": False},
        ],
    },
    {
        "text": "Which Google Cloud service provides serverless computing?",
        "explanation": "Google Cloud Functions is a serverless execution environment for building and connecting cloud services. It automatically scales and only charges for actual usage.",
        "reference": "https://cloud.google.com/functions",
        "points": 1,
        "answers": [
            {"text": "Google Compute Engine", "is_correct": False},
            {"text": "Google Cloud Functions", "is_correct": True},
            {"text": "Google App Engine", "is_correct": False},
            {"text": "Google Cloud Storage", "is_correct": False},
        ],
    },
    {
        "text": "What is Google Cloud Storage used for?",
        "explanation": "Google Cloud Storage is a unified object storage service that provides worldwide storage and retrieval of any amount of data at any time, suitable for backup, archiving, and content distribution.",
        "reference": "https://cloud.google.com/storage",
        "points": 1,
        "answers": [
            {"text": "Running virtual machines", "is_correct": False},
            {"text": "Object storage and file hosting", "is_correct": True},
            {"text": "Database management", "is_correct": False},
            {"text": "Network load balancing", "is_correct": False},
        ],
    },
]
