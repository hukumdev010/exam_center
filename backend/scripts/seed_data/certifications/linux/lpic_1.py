"""Linux Professional Institute Certification Level 1 (LPIC-1)"""

CERTIFICATION = {
    "name": "Linux Professional Institute Certification Level 1 (LPIC-1)",
    "description": "Fundamental Linux administration skills and knowledge",
    "slug": "lpic-1",
    "level": "Associate",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which file contains the system's hostname in most Linux distributions?",
        "explanation": "/etc/hostname contains the system's hostname in most modern Linux distributions.",
        "reference": "https://www.lpi.org/our-certifications/lpic-1-overview",
        "points": 1,
        "answers": [
            {"text": "/etc/hosts", "is_correct": False},
            {"text": "/etc/hostname", "is_correct": True},
            {"text": "/etc/resolv.conf", "is_correct": False},
            {"text": "/etc/network", "is_correct": False}
        ]
    }
]
