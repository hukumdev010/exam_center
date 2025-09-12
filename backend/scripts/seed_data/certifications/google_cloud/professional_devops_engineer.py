"""Google Cloud Professional DevOps Engineer Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional DevOps Engineer",
    "description": "Use Google Cloud to build software delivery pipelines, deploy and monitor services, and manage incidents",
    "slug": "google-professional-devops-engineer",
    "level": "Professional",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "google-cloud",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service is used for continuous integration and deployment pipelines?",
        "explanation": "Cloud Build is a service that executes builds on Google Cloud infrastructure, supporting continuous integration and deployment workflows.",
        "reference": "https://cloud.google.com/build/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Build", "is_correct": True},
            {"text": "Cloud Deploy", "is_correct": False},
            {"text": "Cloud Run", "is_correct": False},
            {"text": "Cloud Functions", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary purpose of Google Cloud Operations Suite (formerly Stackdriver)?",
        "explanation": "Google Cloud Operations Suite provides monitoring, logging, error reporting, and debugging capabilities for applications running on Google Cloud.",
        "reference": "https://cloud.google.com/products/operations",
        "points": 1,
        "answers": [
            {"text": "Code deployment", "is_correct": False},
            {"text": "Monitoring and observability", "is_correct": True},
            {"text": "Data storage", "is_correct": False},
            {"text": "Network configuration", "is_correct": False}
        ]
    },
    {
        "text": "Which tool is recommended for Infrastructure as Code on Google Cloud?",
        "explanation": "Terraform is the recommended tool for Infrastructure as Code on Google Cloud, with extensive provider support for Google Cloud resources.",
        "reference": "https://cloud.google.com/docs/terraform",
        "points": 1,
        "answers": [
            {"text": "Cloud Shell", "is_correct": False},
            {"text": "Terraform", "is_correct": True},
            {"text": "gcloud CLI", "is_correct": False},
            {"text": "Cloud Console", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Cloud Source Repositories?",
        "explanation": "Cloud Source Repositories provides fully managed private Git repositories hosted on Google Cloud, integrated with other Google Cloud services.",
        "reference": "https://cloud.google.com/source-repositories/docs",
        "points": 1,
        "answers": [
            {"text": "Container registry", "is_correct": False},
            {"text": "Git repository hosting", "is_correct": True},
            {"text": "Application deployment", "is_correct": False},
            {"text": "Secret management", "is_correct": False}
        ]
    },
    {
        "text": "Which Google Cloud service helps with progressive deployment strategies?",
        "explanation": "Cloud Deploy provides managed continuous delivery with support for deployment strategies like canary deployments and blue-green deployments.",
        "reference": "https://cloud.google.com/deploy/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Build", "is_correct": False},
            {"text": "Cloud Deploy", "is_correct": True},
            {"text": "GKE", "is_correct": False},
            {"text": "Cloud Run", "is_correct": False}
        ]
    }
]
