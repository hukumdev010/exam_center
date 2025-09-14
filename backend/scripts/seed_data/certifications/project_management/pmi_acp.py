"""PMI Agile Certified Practitioner (PMI-ACP) Certification"""

CERTIFICATION = {
    "name": "PMI Agile Certified Practitioner (PMI-ACP)",
    "description": "Validates knowledge of agile principles, practices, tools, and techniques across agile methodologies",
    "slug": "pmi-agile-certified-practitioner-acp",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "project-management",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the primary focus of the Agile Manifesto?",
        "explanation": "The Agile Manifesto emphasizes individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan.",
        "reference": "https://agilemanifesto.org/",
        "points": 1,
        "answers": [
            {"text": "Comprehensive documentation", "is_correct": False},
            {
                "text": "Individuals and interactions over processes and tools",
                "is_correct": True,
            },
            {"text": "Contract negotiation", "is_correct": False},
            {"text": "Following a strict plan", "is_correct": False},
        ],
    },
    {
        "text": "In Scrum, what is the maximum recommended duration for a Sprint?",
        "explanation": "According to the Scrum Guide, Sprints have a maximum duration of one month (4 weeks). Shorter Sprints are often used to limit risk and enable more frequent feedback.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "2 weeks", "is_correct": False},
            {"text": "4 weeks (1 month)", "is_correct": True},
            {"text": "6 weeks", "is_correct": False},
            {"text": "8 weeks", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of a retrospective in agile methodologies?",
        "explanation": "Retrospectives are held to reflect on the most recent iteration and identify improvements for future iterations. It's about continuous improvement of the team's process and effectiveness.",
        "reference": "https://www.agilealliance.org/glossary/heartbeatretro/",
        "points": 1,
        "answers": [
            {"text": "To plan the next iteration", "is_correct": False},
            {
                "text": "To identify improvements for future iterations",
                "is_correct": True,
            },
            {"text": "To review completed features", "is_correct": False},
            {"text": "To estimate user stories", "is_correct": False},
        ],
    },
    {
        "text": "Which principle is fundamental to Kanban?",
        "explanation": "Kanban is based on visualizing work, limiting work in progress (WIP), and managing flow. The visual board helps teams see the flow of work and identify bottlenecks.",
        "reference": "https://www.agilealliance.org/glossary/kanban/",
        "points": 1,
        "answers": [
            {"text": "Fixed iterations", "is_correct": False},
            {"text": "Visualizing work and limiting WIP", "is_correct": True},
            {"text": "Daily standups", "is_correct": False},
            {"text": "Sprint planning", "is_correct": False},
        ],
    },
    {
        "text": "What does 'velocity' measure in agile project management?",
        "explanation": "Velocity measures the amount of work a team can complete during a single Sprint/iteration. It's typically measured in story points or other estimation units and helps with Sprint planning.",
        "reference": "https://www.agilealliance.org/glossary/velocity/",
        "points": 1,
        "answers": [
            {"text": "Team satisfaction", "is_correct": False},
            {"text": "Amount of work completed per Sprint", "is_correct": True},
            {"text": "Code quality", "is_correct": False},
            {"text": "Customer satisfaction", "is_correct": False},
        ],
    },
]
