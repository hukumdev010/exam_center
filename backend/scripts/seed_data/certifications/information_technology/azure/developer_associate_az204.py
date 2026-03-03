"""Azure Developer Associate Certification"""

CERTIFICATION = {
    "name": "Azure Developer Associate",
    "description": "Develop cloud solutions on Azure",
    "slug": "azure-developer-associate-az204",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "azure",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Azure service is used for serverless computing and event-driven applications?",
        "explanation": "Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure.",
        "reference": "https://docs.microsoft.com/en-us/azure/azure-functions/",
        "points": 1,
        "answers": [
            {"text": "Azure App Service", "is_correct": False},
            {"text": "Azure Functions", "is_correct": True},
            {"text": "Azure Container Instances", "is_correct": False},
            {"text": "Azure Batch", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure App Service primarily used for?",
        "explanation": "Azure App Service is a fully managed platform for building, deploying, and scaling web apps, mobile app backends, and RESTful APIs without managing infrastructure.",
        "reference": "https://docs.microsoft.com/en-us/azure/app-service/",
        "points": 1,
        "answers": [
            {"text": "Database hosting", "is_correct": False},
            {"text": "Web application hosting and deployment", "is_correct": True},
            {"text": "Virtual machine management", "is_correct": False},
            {"text": "File storage", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides managed container orchestration?",
        "explanation": "Azure Kubernetes Service (AKS) provides managed Kubernetes container orchestration, simplifying deployment and management of containerized applications.",
        "reference": "https://docs.microsoft.com/en-us/azure/aks/",
        "points": 1,
        "answers": [
            {"text": "Azure Container Registry", "is_correct": False},
            {"text": "Azure Kubernetes Service (AKS)", "is_correct": True},
            {"text": "Azure Container Instances", "is_correct": False},
            {"text": "Azure Service Fabric", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Key Vault used for?",
        "explanation": "Azure Key Vault is used to securely store and access secrets, keys, and certificates. It provides centralized management of application secrets with secure access control.",
        "reference": "https://docs.microsoft.com/en-us/azure/key-vault/",
        "points": 1,
        "answers": [
            {"text": "Data backup", "is_correct": False},
            {"text": "Secure secrets and key management", "is_correct": True},
            {"text": "Application monitoring", "is_correct": False},
            {"text": "Load balancing", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service is used for application performance monitoring and diagnostics?",
        "explanation": "Azure Application Insights is an Application Performance Management (APM) service that provides monitoring, diagnostics, and analytics for web applications.",
        "reference": "https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview",
        "points": 1,
        "answers": [
            {"text": "Azure Monitor", "is_correct": False},
            {"text": "Azure Application Insights", "is_correct": True},
            {"text": "Azure Log Analytics", "is_correct": False},
            {"text": "Azure Security Center", "is_correct": False},
        ],
    },
]
