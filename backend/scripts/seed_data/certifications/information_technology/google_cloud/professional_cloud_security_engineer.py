"""Google Cloud Professional Cloud Security Engineer Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional Cloud Security Engineer",
    "description": "Configure access within a cloud solution environment and ensure compliance with security policies",
    "slug": "google-professional-cloud-security-engineer",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "google-cloud",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service provides centralized secret management?",
        "explanation": "Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data on Google Cloud.",
        "reference": "https://cloud.google.com/secret-manager/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud KMS", "is_correct": False},
            {"text": "Secret Manager", "is_correct": True},
            {"text": "Cloud IAM", "is_correct": False},
            {"text": "Cloud Security Center", "is_correct": False},
        ],
    },
    {
        "text": "What is the primary purpose of Cloud Key Management Service (KMS)?",
        "explanation": "Cloud KMS allows you to create, import, and manage cryptographic keys and use them to encrypt and decrypt data in Google Cloud services.",
        "reference": "https://cloud.google.com/kms/docs",
        "points": 1,
        "answers": [
            {"text": "User authentication", "is_correct": False},
            {"text": "Cryptographic key management", "is_correct": True},
            {"text": "Network security", "is_correct": False},
            {"text": "Access logging", "is_correct": False},
        ],
    },
    {
        "text": "Which service provides security insights and recommendations for Google Cloud resources?",
        "explanation": "Security Command Center provides centralized visibility into security findings, vulnerabilities, and compliance across Google Cloud assets.",
        "reference": "https://cloud.google.com/security-command-center/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Asset Inventory", "is_correct": False},
            {"text": "Security Command Center", "is_correct": True},
            {"text": "Cloud Audit Logs", "is_correct": False},
            {"text": "Cloud Identity", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of VPC Service Controls?",
        "explanation": "VPC Service Controls helps mitigate data exfiltration risks by creating security perimeters around Google Cloud resources and services.",
        "reference": "https://cloud.google.com/vpc-service-controls/docs",
        "points": 1,
        "answers": [
            {"text": "Network routing", "is_correct": False},
            {"text": "Data exfiltration protection", "is_correct": True},
            {"text": "Load balancing", "is_correct": False},
            {"text": "DNS resolution", "is_correct": False},
        ],
    },
    {
        "text": "Which Google Cloud service provides web application firewall capabilities?",
        "explanation": "Cloud Armor provides DDoS protection and web application firewall (WAF) capabilities for applications running on Google Cloud.",
        "reference": "https://cloud.google.com/armor/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud CDN", "is_correct": False},
            {"text": "Cloud Armor", "is_correct": True},
            {"text": "Cloud Load Balancing", "is_correct": False},
            {"text": "VPC Firewall", "is_correct": False},
        ],
    },
]
