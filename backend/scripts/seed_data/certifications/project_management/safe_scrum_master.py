"""SAFe Scrum Master Certification"""

CERTIFICATION = {
    "name": "SAFe Scrum Master",
    "description": "Scaled Agile Framework expertise for Scrum Masters in enterprise environments",
    "slug": "safe-scrum-master",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "project-management",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the primary role of a Scrum Master in SAFe?",
        "explanation": "In SAFe, the Scrum Master serves the team by facilitating team events, removing impediments, and helping the team improve their practices while supporting the broader Agile Release Train.",
        "reference": "https://scaledagileframework.com/scrum-master/",
        "points": 1,
        "answers": [
            {"text": "Managing the team's backlog", "is_correct": False},
            {
                "text": "Facilitating team events and removing impediments",
                "is_correct": True,
            },
            {"text": "Making technical decisions", "is_correct": False},
            {"text": "Assigning tasks to team members", "is_correct": False},
        ],
    },
    {
        "text": "What is an Agile Release Train (ART) in SAFe?",
        "explanation": "An Agile Release Train is a long-lived team of Agile teams that work together to deliver value in a value stream. ARTs are typically 50-125 people and deliver solutions incrementally.",
        "reference": "https://scaledagileframework.com/agile-release-train/",
        "points": 1,
        "answers": [
            {"text": "A single Scrum team", "is_correct": False},
            {
                "text": "A collection of Agile teams working together",
                "is_correct": True,
            },
            {"text": "A project management tool", "is_correct": False},
            {"text": "A type of user story", "is_correct": False},
        ],
    },
    {
        "text": "How long is a typical Program Increment (PI) in SAFe?",
        "explanation": "A Program Increment is typically 8-12 weeks long and consists of multiple 2-week iterations. It provides a predictable cadence for planning and delivery at the program level.",
        "reference": "https://scaledagileframework.com/program-increment/",
        "points": 1,
        "answers": [
            {"text": "2-4 weeks", "is_correct": False},
            {"text": "8-12 weeks", "is_correct": True},
            {"text": "6 months", "is_correct": False},
            {"text": "1 year", "is_correct": False},
        ],
    },
    {
        "text": "What happens during PI Planning in SAFe?",
        "explanation": "PI Planning is a face-to-face event where all teams in the ART plan the work for the upcoming Program Increment. Teams create their iteration plans, identify dependencies, and commit to objectives.",
        "reference": "https://scaledagileframework.com/pi-planning/",
        "points": 1,
        "answers": [
            {"text": "Individual team sprint planning", "is_correct": False},
            {
                "text": "ART-level planning for the upcoming Program Increment",
                "is_correct": True,
            },
            {"text": "Annual budget planning", "is_correct": False},
            {"text": "Performance reviews", "is_correct": False},
        ],
    },
    {
        "text": "What is the Scrum Master's role during the Inspect and Adapt (I&A) event?",
        "explanation": "During I&A, the Scrum Master helps facilitate the retrospective portion and supports the team in identifying improvement items. They ensure the team's voice is heard in the broader ART improvement process.",
        "reference": "https://scaledagileframework.com/inspect-and-adapt/",
        "points": 1,
        "answers": [
            {"text": "Present demo to stakeholders", "is_correct": False},
            {
                "text": "Facilitate retrospective and support team improvement",
                "is_correct": True,
            },
            {"text": "Plan next PI objectives", "is_correct": False},
            {"text": "Conduct performance evaluations", "is_correct": False},
        ],
    },
]
