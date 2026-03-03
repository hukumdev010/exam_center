"""CompTIA Security+ Certification"""

CERTIFICATION = {
    "name": "CompTIA Security+",
    "description": "Foundational cybersecurity skills and knowledge",
    "slug": "comptia-security-plus",
    "level": "Entry",
    "duration": 6,
    "questions_count": 2,
    "category_slug": "cybersecurity",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does CIA stand for in information security?",
        "explanation": "CIA stands for Confidentiality, Integrity, and Availability - the three fundamental principles of information security.",
        "reference": "https://www.nist.gov/cybersecurity",
        "points": 1,
        "answers": [
            {"text": "Central Intelligence Agency", "is_correct": False},
            {"text": "Confidentiality, Integrity, Availability", "is_correct": True},
            {"text": "Computer Information Access", "is_correct": False},
            {"text": "Cyber Intelligence Analytics", "is_correct": False},
        ],
    },
    {
        "text": "Which type of attack involves overwhelming a system with traffic?",
        "explanation": "A Denial of Service (DoS) attack attempts to make a system unavailable by overwhelming it with traffic or requests.",
        "reference": "https://www.cisa.gov/uscert/ncas/tips/ST04-015",
        "points": 1,
        "answers": [
            {"text": "SQL Injection", "is_correct": False},
            {"text": "Cross-Site Scripting", "is_correct": False},
            {"text": "Denial of Service", "is_correct": True},
            {"text": "Man-in-the-Middle", "is_correct": False},
        ],
    },
]
