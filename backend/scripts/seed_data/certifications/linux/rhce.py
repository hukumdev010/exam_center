"""Red Hat Certified Engineer (RHCE) Certification"""

CERTIFICATION = {
    "name": "Red Hat Certified Engineer (RHCE)",
    "description": "Advanced Red Hat Enterprise Linux administration and automation",
    "slug": "rhce",
    "level": "Expert",
    "duration": 210,
    "questions_count": 15,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which tool is primarily used for automation in RHCE certification?",
        "explanation": "Ansible is the primary automation tool covered in RHCE certification for automating deployment and configuration management.",
        "reference": "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/administration_guide/",
        "points": 1,
        "answers": [
            {"text": "Puppet", "is_correct": False},
            {"text": "Ansible", "is_correct": True},
            {"text": "Chef", "is_correct": False},
            {"text": "SaltStack", "is_correct": False}
        ]
    }
]
