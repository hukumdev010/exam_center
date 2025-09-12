"""PRINCE2 Foundation Certification"""

CERTIFICATION = {
    "name": "PRINCE2 Foundation",
    "description": "Demonstrates understanding of PRINCE2 methodology for structured project management",
    "slug": "prince2-foundation",
    "level": "Associate",
    "duration": 60,
    "questions_count": 60,
    "category_slug": "project-management",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "How many principles does PRINCE2 have?",
        "explanation": "PRINCE2 has 7 principles that guide and inform project management decisions. These principles are universal and apply to all projects regardless of type, size, or complexity.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "5", "is_correct": False},
            {"text": "7", "is_correct": True},
            {"text": "9", "is_correct": False},
            {"text": "12", "is_correct": False}
        ]
    },
    {
        "text": "What does the principle 'Manage by Stages' mean in PRINCE2?",
        "explanation": "Manage by Stages means that PRINCE2 projects are planned, monitored and controlled on a stage-by-stage basis. This enables better control and decision-making at key points.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Projects should have multiple teams", "is_correct": False},
            {"text": "Projects are planned and controlled stage-by-stage", "is_correct": True},
            {"text": "All work must be done in sequence", "is_correct": False},
            {"text": "Stages should be equal in length", "is_correct": False}
        ]
    },
    {
        "text": "Which PRINCE2 theme addresses the question 'What is the project aiming to achieve'?",
        "explanation": "The Business Case theme addresses what the project is aiming to achieve and why it is worthwhile to invest in the project. It establishes the justification for the project.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Organization", "is_correct": False},
            {"text": "Business Case", "is_correct": True},
            {"text": "Quality", "is_correct": False},
            {"text": "Plans", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of the Project Board in PRINCE2?",
        "explanation": "The Project Board is the project's steering committee responsible for making key decisions, providing direction, and ensuring the project remains viable and aligned with business objectives.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "Execute project work", "is_correct": False},
            {"text": "Provide project direction and key decisions", "is_correct": True},
            {"text": "Create detailed plans", "is_correct": False},
            {"text": "Manage daily operations", "is_correct": False}
        ]
    },
    {
        "text": "How many processes are there in PRINCE2?",
        "explanation": "PRINCE2 has 7 processes that take a project from start to finish: Starting up a Project, Directing a Project, Initiating a Project, Controlling a Stage, Managing Product Delivery, Managing a Stage Boundary, and Closing a Project.",
        "reference": "https://www.prince2.com/eur/what-is-prince2",
        "points": 1,
        "answers": [
            {"text": "5", "is_correct": False},
            {"text": "7", "is_correct": True},
            {"text": "9", "is_correct": False},
            {"text": "10", "is_correct": False}
        ]
    }
]
