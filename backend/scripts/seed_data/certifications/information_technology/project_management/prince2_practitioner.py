"""PRINCE2 Practitioner Certification"""

CERTIFICATION = {
    "name": "PRINCE2 Practitioner",
    "description": "Advanced application of PRINCE2 methodology in real project scenarios",
    "slug": "prince2-practitioner",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "project-management",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which technique is used in PRINCE2 to identify and assess project risks?",
        "explanation": "PRINCE2 uses Risk Register as the key technique to identify, assess, and manage project risks throughout the project lifecycle. It includes probability, impact, and response strategies.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "SWOT Analysis", "is_correct": False},
            {"text": "Risk Register", "is_correct": True},
            {"text": "Monte Carlo Simulation", "is_correct": False},
            {"text": "Decision Tree", "is_correct": False},
        ],
    },
    {
        "text": "When should tolerance levels be set in a PRINCE2 project?",
        "explanation": "Tolerance levels should be set during project initiation and stage planning. They define the permissible deviation from planned targets without escalating to the next management level.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Only at project closure", "is_correct": False},
            {"text": "During initiation and stage planning", "is_correct": True},
            {"text": "After problems occur", "is_correct": False},
            {"text": "Only for major milestones", "is_correct": False},
        ],
    },
    {
        "text": "What is the primary purpose of the Quality Register in PRINCE2?",
        "explanation": "The Quality Register provides a summary of all planned and completed quality activities, including quality reviews, tests, and audits. It ensures quality activities are tracked and executed.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Track project costs", "is_correct": False},
            {
                "text": "Summary of planned and completed quality activities",
                "is_correct": True,
            },
            {"text": "Monitor team performance", "is_correct": False},
            {"text": "Record stakeholder feedback", "is_correct": False},
        ],
    },
    {
        "text": "In PRINCE2, what should happen when a stage tolerance is forecast to be exceeded?",
        "explanation": "When stage tolerance is forecast to be exceeded, an Exception Report should be prepared and sent to the Project Board, along with options for how to proceed. This triggers the Exception process.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Continue as normal", "is_correct": False},
            {"text": "Prepare Exception Report for Project Board", "is_correct": True},
            {"text": "Increase the tolerance", "is_correct": False},
            {"text": "Stop the project immediately", "is_correct": False},
        ],
    },
    {
        "text": "Which PRINCE2 technique helps ensure products meet quality requirements?",
        "explanation": "Quality Review Technique is a structured approach in PRINCE2 to check that products meet their quality criteria. It involves reviewers examining products against defined quality criteria.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Product Breakdown Structure", "is_correct": False},
            {"text": "Quality Review Technique", "is_correct": True},
            {"text": "Change Control", "is_correct": False},
            {"text": "Configuration Management", "is_correct": False},
        ],
    },
]
