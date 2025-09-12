"""GCIH (GIAC Certified Incident Handler) Certification"""

CERTIFICATION = {
    "name": "GCIH - GIAC Certified Incident Handler",
    "description": "Skills to detect, respond to, and resolve computer security incidents",
    "slug": "giac-gcih",
    "level": "Intermediate",
    "duration": 180,
    "questions_count": 106,
    "category_slug": "cybersecurity",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the first step in the incident response process?",
        "explanation": "Preparation is the first step in incident response, involving establishing policies, procedures, and capabilities to effectively handle security incidents.",
        "reference": "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final",
        "points": 1,
        "answers": [
            {"text": "Preparation", "is_correct": True},
            {"text": "Detection and Analysis", "is_correct": False},
            {"text": "Containment", "is_correct": False},
            {"text": "Recovery", "is_correct": False}
        ]
    },
    {
        "text": "Which tool is commonly used for network packet analysis?",
        "explanation": "Wireshark is a network protocol analyzer that captures and displays network packets in real-time, making it essential for incident analysis and network troubleshooting.",
        "reference": "https://www.wireshark.org/docs/",
        "points": 1,
        "answers": [
            {"text": "Wireshark", "is_correct": True},
            {"text": "Metasploit", "is_correct": False},
            {"text": "Nessus", "is_correct": False},
            {"text": "John the Ripper", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of forensic imaging?",
        "explanation": "Forensic imaging creates a bit-for-bit copy of storage media to preserve evidence while allowing analysis on the copy rather than the original evidence.",
        "reference": "https://www.sans.org/reading-room/whitepapers/incident/digital-forensics-incident-response-2242",
        "points": 1,
        "answers": [
            {"text": "Create exact copies of storage media for analysis", "is_correct": True},
            {"text": "Enhance image quality", "is_correct": False},
            {"text": "Compress files", "is_correct": False},
            {"text": "Delete evidence", "is_correct": False}
        ]
    },
    {
        "text": "Which Windows log file typically contains logon/logoff events?",
        "explanation": "The Windows Security log contains audit events including logon/logoff activities, privilege use, and other security-related events that are crucial for incident investigation.",
        "reference": "https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-log-service-overview",
        "points": 1,
        "answers": [
            {"text": "Security log", "is_correct": True},
            {"text": "Application log", "is_correct": False},
            {"text": "System log", "is_correct": False},
            {"text": "Setup log", "is_correct": False}
        ]
    },
    {
        "text": "What is indicators of compromise (IoCs)?",
        "explanation": "Indicators of Compromise (IoCs) are pieces of forensic data that identify potentially malicious activity on a system or network, such as file hashes, IP addresses, or domain names.",
        "reference": "https://www.sans.org/reading-room/whitepapers/detection/indicators-compromise-36352",
        "points": 1,
        "answers": [
            {"text": "Forensic artifacts that indicate potential security breaches", "is_correct": True},
            {"text": "Software vulnerabilities", "is_correct": False},
            {"text": "Network configuration errors", "is_correct": False},
            {"text": "User account permissions", "is_correct": False}
        ]
    }
]
