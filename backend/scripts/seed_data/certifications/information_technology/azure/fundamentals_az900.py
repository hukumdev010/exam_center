"""Microsoft Azure Fundamentals Certification"""

CERTIFICATION = {
    "name": "Microsoft Azure Fundamentals",
    "description": "Foundational knowledge of Azure cloud concepts",
    "slug": "azure-fundamentals-az900",
    "level": "Foundational",
    "duration": 9,
    "questions_count": 3,
    "category_slug": "azure",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What are the three main categories of cloud services?",
        "explanation": "The three main cloud service categories are Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).",
        "reference": "https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/",
        "points": 1,
        "answers": [
            {"text": "IaaS, PaaS, SaaS", "is_correct": True},
            {"text": "Public, Private, Hybrid", "is_correct": False},
            {"text": "Compute, Storage, Network", "is_correct": False},
            {"text": "Basic, Standard, Premium", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides serverless compute?",
        "explanation": "Azure Functions provides serverless compute that lets you run code on-demand without having to explicitly provision or manage infrastructure.",
        "reference": "https://docs.microsoft.com/en-us/azure/azure-functions/",
        "points": 1,
        "answers": [
            {"text": "Azure Virtual Machines", "is_correct": False},
            {"text": "Azure Functions", "is_correct": True},
            {"text": "Azure Container Instances", "is_correct": False},
            {"text": "Azure App Service", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Resource Manager (ARM)?",
        "explanation": "Azure Resource Manager is the deployment and management service for Azure. It provides a consistent management layer that enables you to create, update, and delete resources.",
        "reference": "https://docs.microsoft.com/en-us/azure/azure-resource-manager/",
        "points": 1,
        "answers": [
            {"text": "A monitoring service", "is_correct": False},
            {"text": "A deployment and management service", "is_correct": True},
            {"text": "A storage service", "is_correct": False},
            {"text": "A networking service", "is_correct": False},
        ],
    },
]
