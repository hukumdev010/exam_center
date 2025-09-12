"""Palo Alto Networks Certified Network Security Engineer (PCNSE) Certification"""

CERTIFICATION = {
    "name": "Palo Alto Networks Certified Network Security Engineer (PCNSE)",
    "description": "Advanced network security using Palo Alto Networks technologies",
    "slug": "palo-alto-pcnse",
    "level": "Professional",
    "duration": 80,
    "questions_count": 75,
    "category_slug": "networking",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary function of App-ID in Palo Alto Networks firewalls?",
        "explanation": "App-ID identifies applications traversing the network regardless of port, protocol, or encryption, enabling application-based security policies.",
        "reference": "https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/app-id",
        "points": 1,
        "answers": [
            {"text": "User identification", "is_correct": False},
            {"text": "Application identification", "is_correct": True},
            {"text": "Content filtering", "is_correct": False},
            {"text": "Threat prevention", "is_correct": False}
        ]
    },
    {
        "text": "Which Palo Alto Networks feature provides automated threat intelligence updates?",
        "explanation": "WildFire is Palo Alto Networks' cloud-based threat analysis service that provides automated threat intelligence and protection against unknown malware.",
        "reference": "https://docs.paloaltonetworks.com/wildfire",
        "points": 1,
        "answers": [
            {"text": "Panorama", "is_correct": False},
            {"text": "WildFire", "is_correct": True},
            {"text": "GlobalProtect", "is_correct": False},
            {"text": "User-ID", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Security Profiles in PAN-OS?",
        "explanation": "Security Profiles provide additional security checks including antivirus, anti-spyware, vulnerability protection, URL filtering, file blocking, and data filtering.",
        "reference": "https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/threat-prevention",
        "points": 1,
        "answers": [
            {"text": "Network routing", "is_correct": False},
            {"text": "Threat prevention and content security", "is_correct": True},
            {"text": "User authentication", "is_correct": False},
            {"text": "Quality of Service", "is_correct": False}
        ]
    },
    {
        "text": "Which zone type is used for external untrusted networks in Palo Alto Networks?",
        "explanation": "External zones are typically used to represent untrusted networks such as the Internet, where security policies are more restrictive.",
        "reference": "https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/networking/configure-interfaces/interface-management-profiles",
        "points": 1,
        "answers": [
            {"text": "Internal", "is_correct": False},
            {"text": "External", "is_correct": True},
            {"text": "DMZ", "is_correct": False},
            {"text": "Tap", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary benefit of GlobalProtect in Palo Alto Networks?",
        "explanation": "GlobalProtect extends the Next-Generation Firewall protection to remote users and mobile devices, ensuring consistent security policies regardless of location.",
        "reference": "https://docs.paloaltonetworks.com/globalprotect",
        "points": 1,
        "answers": [
            {"text": "Central management", "is_correct": False},
            {"text": "Remote access VPN and endpoint protection", "is_correct": True},
            {"text": "Threat analysis", "is_correct": False},
            {"text": "Application control", "is_correct": False}
        ]
    }
]
