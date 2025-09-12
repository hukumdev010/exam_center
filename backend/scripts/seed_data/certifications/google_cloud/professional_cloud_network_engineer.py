"""Google Cloud Professional Cloud Network Engineer Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional Cloud Network Engineer",
    "description": "Implement and manage network architectures in Google Cloud Platform",
    "slug": "google-professional-cloud-network-engineer",
    "level": "Professional",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "google-cloud",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service provides private connectivity to Google services?",
        "explanation": "Private Google Access allows instances in a VPC subnet to reach Google APIs and services using private IP addresses instead of external IP addresses.",
        "reference": "https://cloud.google.com/vpc/docs/private-google-access",
        "points": 1,
        "answers": [
            {"text": "Cloud VPN", "is_correct": False},
            {"text": "Private Google Access", "is_correct": True},
            {"text": "Cloud Interconnect", "is_correct": False},
            {"text": "Cloud NAT", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary benefit of using Cloud Interconnect?",
        "explanation": "Cloud Interconnect provides enterprise-grade connections between on-premises infrastructure and Google Cloud with higher bandwidth and lower latency than VPN.",
        "reference": "https://cloud.google.com/network-connectivity/docs/interconnect",
        "points": 1,
        "answers": [
            {"text": "Cost reduction", "is_correct": False},
            {"text": "High bandwidth, low latency connectivity", "is_correct": True},
            {"text": "Enhanced security", "is_correct": False},
            {"text": "Automatic scaling", "is_correct": False}
        ]
    },
    {
        "text": "Which load balancer type is best for global HTTP(S) traffic distribution?",
        "explanation": "Global HTTP(S) Load Balancer distributes traffic across multiple regions and provides features like SSL termination, URL maps, and backend services.",
        "reference": "https://cloud.google.com/load-balancing/docs/https",
        "points": 1,
        "answers": [
            {"text": "Regional TCP Load Balancer", "is_correct": False},
            {"text": "Global HTTP(S) Load Balancer", "is_correct": True},
            {"text": "Internal Load Balancer", "is_correct": False},
            {"text": "Network Load Balancer", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Cloud NAT?",
        "explanation": "Cloud NAT provides managed network address translation for instances without external IP addresses to access the internet and external services.",
        "reference": "https://cloud.google.com/nat/docs",
        "points": 1,
        "answers": [
            {"text": "Load balancing", "is_correct": False},
            {"text": "Outbound internet access for private instances", "is_correct": True},
            {"text": "DNS resolution", "is_correct": False},
            {"text": "VPN connectivity", "is_correct": False}
        ]
    },
    {
        "text": "Which Google Cloud service provides content delivery network capabilities?",
        "explanation": "Cloud CDN accelerates content delivery by caching content at Google's globally distributed edge points of presence, reducing latency for users.",
        "reference": "https://cloud.google.com/cdn/docs",
        "points": 1,
        "answers": [
            {"text": "Cloud Storage", "is_correct": False},
            {"text": "Cloud CDN", "is_correct": True},
            {"text": "Cloud Load Balancing", "is_correct": False},
            {"text": "Cloud Armor", "is_correct": False}
        ]
    }
]
