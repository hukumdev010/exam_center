"""Fortinet Network Security Expert (NSE) Certification"""

CERTIFICATION = {
    "name": "Fortinet Network Security Expert (NSE)",
    "description": "Advanced network security using Fortinet FortiGate technologies",
    "slug": "fortinet-nse",
    "level": "Professional",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "networking",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary function of FortiGate's Security Fabric?",
        "explanation": "Security Fabric provides broad, integrated, and automated cybersecurity protection across the entire digital attack surface by connecting Fortinet security solutions.",
        "reference": "https://docs.fortinet.com/document/fortigate/7.2.0/administration-guide/954635/security-fabric",
        "points": 1,
        "answers": [
            {"text": "Load balancing", "is_correct": False},
            {"text": "Integrated security architecture", "is_correct": True},
            {"text": "Network routing", "is_correct": False},
            {"text": "Content filtering", "is_correct": False}
        ]
    },
    {
        "text": "Which FortiGate feature provides application control and identification?",
        "explanation": "Application Control in FortiGate identifies and controls applications regardless of port or protocol, allowing administrators to create granular security policies.",
        "reference": "https://docs.fortinet.com/document/fortigate/7.2.0/administration-guide/891236/application-control",
        "points": 1,
        "answers": [
            {"text": "Web Filter", "is_correct": False},
            {"text": "Application Control", "is_correct": True},
            {"text": "IPS", "is_correct": False},
            {"text": "SSL Inspection", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of FortiGuard services?",
        "explanation": "FortiGuard provides real-time threat intelligence, security updates, and cloud-based security services to enhance FortiGate protection capabilities.",
        "reference": "https://www.fortiguard.com/services",
        "points": 1,
        "answers": [
            {"text": "Hardware monitoring", "is_correct": False},
            {"text": "Threat intelligence and security updates", "is_correct": True},
            {"text": "Network optimization", "is_correct": False},
            {"text": "User authentication", "is_correct": False}
        ]
    },
    {
        "text": "Which FortiGate operating mode provides the highest level of security inspection?",
        "explanation": "Flow-based inspection mode (default) provides comprehensive security features including full UTM capabilities, while proxy-based mode offers even deeper inspection for specific protocols.",
        "reference": "https://docs.fortinet.com/document/fortigate/7.2.0/administration-guide/397979/inspection-modes",
        "points": 1,
        "answers": [
            {"text": "NAT mode", "is_correct": False},
            {"text": "Flow-based inspection", "is_correct": True},
            {"text": "Transparent mode", "is_correct": False},
            {"text": "Bridge mode", "is_correct": False}
        ]
    },
    {
        "text": "What is the function of FortiAnalyzer in Fortinet's ecosystem?",
        "explanation": "FortiAnalyzer provides centralized logging, reporting, and analytics for Fortinet security devices, offering comprehensive visibility into network security events.",
        "reference": "https://docs.fortinet.com/product/fortianalyzer",
        "points": 1,
        "answers": [
            {"text": "Firewall management", "is_correct": False},
            {"text": "Centralized logging and analytics", "is_correct": True},
            {"text": "Endpoint protection", "is_correct": False},
            {"text": "Network switching", "is_correct": False}
        ]
    }
]
