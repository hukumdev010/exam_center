"""CISCP (Certified Information Systems Cybersecurity Professional) Certification"""

CERTIFICATION = {
    "name": "CISCP - Certified Information Systems Cybersecurity Professional",
    "description": "Advanced cybersecurity expertise covering risk management, security architecture, and incident response",
    "slug": "ciscp-cybersecurity-professional",
    "level": "Professional",
    "duration": 180,
    "questions_count": 125,
    "category_slug": "cybersecurity",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary purpose of a Security Operations Center (SOC)?",
        "explanation": "A Security Operations Center (SOC) is a centralized unit that deals with security issues on an organizational and technical level. It monitors, prevents, detects, investigates, and responds to cyber threats.",
        "reference": "https://www.sans.org/white-papers/39825/",
        "points": 1,
        "answers": [
            {"text": "Monitor and respond to security incidents 24/7", "is_correct": True},
            {"text": "Develop software applications", "is_correct": False},
            {"text": "Manage network infrastructure", "is_correct": False},
            {"text": "Handle customer support", "is_correct": False}
        ]
    },
    {
        "text": "Which framework is commonly used for incident response?",
        "explanation": "The NIST Cybersecurity Framework provides a policy framework of computer security guidance for how private sector organizations can assess and improve their ability to prevent, detect, and respond to cyber attacks.",
        "reference": "https://www.nist.gov/cyberframework",
        "points": 1,
        "answers": [
            {"text": "NIST Cybersecurity Framework", "is_correct": True},
            {"text": "ITIL Framework", "is_correct": False},
            {"text": "Agile Framework", "is_correct": False},
            {"text": "DevOps Framework", "is_correct": False}
        ]
    },
    {
        "text": "What is threat intelligence?",
        "explanation": "Threat intelligence is evidence-based knowledge, including context, mechanisms, indicators, implications and actionable advice, about an existing or emerging menace or hazard to assets that can be used to inform decisions regarding the subject's response to that menace or hazard.",
        "reference": "https://www.sans.org/reading-room/whitepapers/analyst/defining-cyber-threat-intelligence-36240",
        "points": 1,
        "answers": [
            {"text": "Data about potential security threats and attackers", "is_correct": True},
            {"text": "Software for monitoring networks", "is_correct": False},
            {"text": "Hardware security modules", "is_correct": False},
            {"text": "Encryption algorithms", "is_correct": False}
        ]
    },
    {
        "text": "Which type of analysis examines malware in a controlled environment?",
        "explanation": "Dynamic analysis involves executing malware in a controlled environment (sandbox) to observe its behavior, while static analysis examines the code without executing it.",
        "reference": "https://www.sans.org/reading-room/whitepapers/malicious/paper/2136",
        "points": 1,
        "answers": [
            {"text": "Dynamic analysis", "is_correct": True},
            {"text": "Static analysis", "is_correct": False},
            {"text": "Behavioral analysis", "is_correct": False},
            {"text": "Forensic analysis", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of a honeypot in cybersecurity?",
        "explanation": "A honeypot is a security mechanism set to detect, deflect, or counteract attempts at unauthorized use of information systems. It appears to be a legitimate system but is actually isolated and monitored.",
        "reference": "https://www.sans.org/reading-room/whitepapers/detection/deployment-analysis-honeypots-detection-internal-threats-1690",
        "points": 1,
        "answers": [
            {"text": "Attract and monitor attackers", "is_correct": True},
            {"text": "Store encrypted data", "is_correct": False},
            {"text": "Backup system files", "is_correct": False},
            {"text": "Manage user access", "is_correct": False}
        ]
    }
]
