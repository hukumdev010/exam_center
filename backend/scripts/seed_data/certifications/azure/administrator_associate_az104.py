"""Azure Administrator Associate Certification"""

CERTIFICATION = {
    "name": "Azure Administrator Associate",
    "description": "Implement, manage, and monitor Azure environments",
    "slug": "azure-administrator-associate-az104",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "azure",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Azure service is used to manage and deploy Azure resources using declarative templates?",
        "explanation": "Azure Resource Manager (ARM) templates allow you to define and deploy Azure infrastructure using JSON declarative syntax, enabling consistent and repeatable deployments.",
        "reference": "https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/",
        "points": 1,
        "answers": [
            {"text": "Azure PowerShell", "is_correct": False},
            {"text": "Azure Resource Manager (ARM) templates", "is_correct": True},
            {"text": "Azure CLI", "is_correct": False},
            {"text": "Azure Portal", "is_correct": False},
        ],
    },
    {
        "text": "What is the maximum number of storage accounts you can create per Azure subscription by default?",
        "explanation": "By default, you can create up to 250 storage accounts per region per subscription. This limit can be increased by contacting Azure support.",
        "reference": "https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview",
        "points": 1,
        "answers": [
            {"text": "100", "is_correct": False},
            {"text": "200", "is_correct": False},
            {"text": "250", "is_correct": True},
            {"text": "500", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides distributed denial of service (DDoS) protection?",
        "explanation": "Azure DDoS Protection provides DDoS mitigation capabilities. The Basic tier is automatically enabled, while the Standard tier provides additional protection and monitoring features.",
        "reference": "https://docs.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview",
        "points": 1,
        "answers": [
            {"text": "Azure Firewall", "is_correct": False},
            {"text": "Azure DDoS Protection", "is_correct": True},
            {"text": "Azure Security Center", "is_correct": False},
            {"text": "Azure Application Gateway", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Azure Resource Groups?",
        "explanation": "Resource Groups are logical containers that hold related resources for an Azure solution. They provide a way to organize and manage Azure resources collectively, including access control, billing, and lifecycle management.",
        "reference": "https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview",
        "points": 1,
        "answers": [
            {"text": "To store backup data", "is_correct": False},
            {
                "text": "To organize and manage related Azure resources",
                "is_correct": True,
            },
            {"text": "To create virtual networks", "is_correct": False},
            {"text": "To monitor application performance", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service is used for hybrid cloud storage that extends on-premises storage to Azure?",
        "explanation": "Azure Storage Sync enables you to centralize file services in Azure Files while maintaining local access and performance. It synchronizes on-premises Windows Server file shares with Azure file shares.",
        "reference": "https://docs.microsoft.com/en-us/azure/storage/files/storage-sync-files-introduction",
        "points": 1,
        "answers": [
            {"text": "Azure Blob Storage", "is_correct": False},
            {"text": "Azure Storage Sync", "is_correct": True},
            {"text": "Azure Data Lake", "is_correct": False},
            {"text": "Azure Archive Storage", "is_correct": False},
        ],
    },
]
