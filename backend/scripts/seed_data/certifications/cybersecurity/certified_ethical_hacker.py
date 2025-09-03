"""Certified Ethical Hacker (CEH) Certification"""

CERTIFICATION = {
    "name": "Certified Ethical Hacker (CEH)",
    "description": "Ethical hacking and penetration testing",
    "slug": "certified-ethical-hacker-ceh",
    "level": "Professional",
    "duration": 240,
    "questions_count": 125,
    "category_slug": "cybersecurity",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the first phase of ethical hacking?",
        "explanation": "Reconnaissance (or Information Gathering) is the first phase where hackers gather information about the target system.",
        "reference": "https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/",
        "points": 1,
        "answers": [
            {"text": "Scanning", "is_correct": False},
            {"text": "Reconnaissance", "is_correct": True},
            {"text": "Enumeration", "is_correct": False},
            {"text": "System Hacking", "is_correct": False}
        ]
    }
]
