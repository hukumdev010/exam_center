"""Cisco Certified Network Associate (CCNA) Certification"""

CERTIFICATION = {
    "name": "Cisco Certified Network Associate (CCNA)",
    "description": "Networking fundamentals and Cisco technologies",
    "slug": "cisco-ccna",
    "level": "Associate",
    "duration": 3,
    "questions_count": 1,
    "category_slug": "networking",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the default subnet mask for a Class C network?",
        "explanation": "The default subnet mask for Class C networks is 255.255.255.0 or /24 in CIDR notation.",
        "reference": "https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html",
        "points": 1,
        "answers": [
            {"text": "255.255.0.0", "is_correct": False},
            {"text": "255.255.255.0", "is_correct": True},
            {"text": "255.0.0.0", "is_correct": False},
            {"text": "255.255.255.255", "is_correct": False},
        ],
    }
]
