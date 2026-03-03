"""Google Cloud Professional Cloud Architect Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional Cloud Architect",
    "description": "Design, develop, and manage robust, secure, scalable cloud architecture on Google Cloud",
    "slug": "google-professional-cloud-architect",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "google-cloud",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service provides managed Kubernetes clusters?",
        "explanation": "Google Kubernetes Engine (GKE) is a managed Kubernetes service that simplifies deploying, managing, and scaling containerized applications using Google Cloud infrastructure.",
        "reference": "https://cloud.google.com/kubernetes-engine/docs",
        "points": 1,
        "answers": [
            {"text": "Compute Engine", "is_correct": False},
            {"text": "Google Kubernetes Engine (GKE)", "is_correct": True},
            {"text": "Cloud Run", "is_correct": False},
            {"text": "App Engine", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Cloud Load Balancing in Google Cloud?",
        "explanation": "Cloud Load Balancing distributes incoming traffic across multiple instances or regions to ensure high availability, scalability, and performance of applications.",
        "reference": "https://cloud.google.com/load-balancing/docs",
        "points": 1,
        "answers": [
            {"text": "Data storage", "is_correct": False},
            {
                "text": "Distribute traffic across multiple instances",
                "is_correct": True,
            },
            {"text": "Monitor applications", "is_correct": False},
            {"text": "Encrypt data", "is_correct": False},
        ],
    },
    {
        "text": "Which Google Cloud service is best for storing and analyzing large datasets?",
        "explanation": "BigQuery is Google Cloud's fully managed, serverless data warehouse that enables super-fast SQL queries using the processing power of Google's infrastructure.",
        "reference": "https://cloud.google.com/bigquery/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Storage", "is_correct": False},
            {"text": "BigQuery", "is_correct": True},
            {"text": "Cloud SQL", "is_correct": False},
            {"text": "Firestore", "is_correct": False},
        ],
    },
    {
        "text": "What is the primary use case for Google Cloud IAM?",
        "explanation": "Identity and Access Management (IAM) controls who has access to which resources in Google Cloud, providing fine-grained access control and security policies.",
        "reference": "https://cloud.google.com/iam/docs",
        "points": 1,
        "answers": [
            {"text": "Network routing", "is_correct": False},
            {"text": "Access control and security", "is_correct": True},
            {"text": "Data backup", "is_correct": False},
            {"text": "Application deployment", "is_correct": False},
        ],
    },
    {
        "text": "Which Google Cloud networking service provides private connectivity between on-premises and Google Cloud?",
        "explanation": "Cloud VPN provides secure connectivity between on-premises networks and Google Cloud VPC networks through IPsec VPN tunnels.",
        "reference": "https://cloud.google.com/vpn/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud NAT", "is_correct": False},
            {"text": "Cloud VPN", "is_correct": True},
            {"text": "Cloud Router", "is_correct": False},
            {"text": "Cloud DNS", "is_correct": False},
        ],
    },
]
