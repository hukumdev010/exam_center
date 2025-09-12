"""OSCP (Offensive Security Certified Professional) Certification"""

CERTIFICATION = {
    "name": "OSCP - Offensive Security Certified Professional",
    "description": "Hands-on penetration testing certification focusing on practical exploitation skills",
    "slug": "oscp-offensive-security",
    "level": "Advanced",
    "duration": 1440,  # 24 hours
    "questions_count": 0,  # Practical exam
    "category_slug": "cybersecurity",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary methodology taught in the OSCP course?",
        "explanation": "The OSCP focuses on a systematic penetration testing methodology that includes information gathering, vulnerability identification, exploitation, and post-exploitation activities.",
        "reference": "https://www.offensive-security.com/pwk-oscp/",
        "points": 1,
        "answers": [
            {"text": "Systematic penetration testing methodology", "is_correct": True},
            {"text": "Risk assessment framework", "is_correct": False},
            {"text": "Incident response procedures", "is_correct": False},
            {"text": "Compliance auditing", "is_correct": False}
        ]
    },
    {
        "text": "Which tool is commonly used for network enumeration?",
        "explanation": "Nmap (Network Mapper) is a widely used tool for network discovery and security auditing, allowing penetration testers to discover hosts and services on a network.",
        "reference": "https://nmap.org/book/",
        "points": 1,
        "answers": [
            {"text": "Nmap", "is_correct": True},
            {"text": "Wireshark", "is_correct": False},
            {"text": "Burp Suite", "is_correct": False},
            {"text": "John the Ripper", "is_correct": False}
        ]
    },
    {
        "text": "What is privilege escalation?",
        "explanation": "Privilege escalation is the act of exploiting a bug, design flaw or configuration oversight in an operating system or software application to gain elevated access to resources.",
        "reference": "https://attack.mitre.org/tactics/TA0004/",
        "points": 1,
        "answers": [
            {"text": "Gaining higher-level permissions on a compromised system", "is_correct": True},
            {"text": "Creating user accounts", "is_correct": False},
            {"text": "Installing antivirus software", "is_correct": False},
            {"text": "Configuring firewalls", "is_correct": False}
        ]
    },
    {
        "text": "Which framework is commonly used for exploitation?",
        "explanation": "Metasploit is a penetration testing framework that provides information about security vulnerabilities and aids in penetration testing and IDS signature development.",
        "reference": "https://docs.rapid7.com/metasploit/",
        "points": 1,
        "answers": [
            {"text": "Metasploit", "is_correct": True},
            {"text": "NIST Framework", "is_correct": False},
            {"text": "COBIT", "is_correct": False},
            {"text": "ITIL", "is_correct": False}
        ]
    },
    {
        "text": "What is buffer overflow exploitation?",
        "explanation": "Buffer overflow exploitation involves overwriting memory locations to alter program execution flow, often to execute arbitrary code or gain unauthorized access.",
        "reference": "https://owasp.org/www-community/vulnerabilities/Buffer_Overflow",
        "points": 1,
        "answers": [
            {"text": "Overwriting memory to alter program execution", "is_correct": True},
            {"text": "Flooding networks with traffic", "is_correct": False},
            {"text": "Stealing user credentials", "is_correct": False},
            {"text": "Analyzing log files", "is_correct": False}
        ]
    }
]
