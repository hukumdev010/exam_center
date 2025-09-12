"""Professional Scrum Product Owner (PSPO) Certification"""

CERTIFICATION = {
    "name": "Professional Scrum Product Owner (PSPO)",
    "description": "Demonstrates understanding of Product Owner role in Scrum framework and product management principles",
    "slug": "professional-scrum-product-owner-pspo",
    "level": "Professional",
    "duration": 60,
    "questions_count": 80,
    "category_slug": "project-management",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary responsibility of a Product Owner in Scrum?",
        "explanation": "The Product Owner is responsible for maximizing the value of the product resulting from work of the Scrum Team. This includes managing the Product Backlog and ensuring the team works on the most valuable items.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Managing the Scrum Team", "is_correct": False},
            {"text": "Maximizing the value of the product", "is_correct": True},
            {"text": "Writing code", "is_correct": False},
            {"text": "Conducting daily standups", "is_correct": False}
        ]
    },
    {
        "text": "Who is responsible for prioritizing the Product Backlog?",
        "explanation": "The Product Owner is solely responsible for managing and prioritizing the Product Backlog to maximize value and ensure the most important items are worked on first.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Scrum Master", "is_correct": False},
            {"text": "Product Owner", "is_correct": True},
            {"text": "Development Team", "is_correct": False},
            {"text": "Stakeholders", "is_correct": False}
        ]
    },
    {
        "text": "What should Product Backlog items include to be considered 'Ready'?",
        "explanation": "Ready items typically include clear acceptance criteria, sufficient detail for the team to understand and estimate the work, and dependencies identified. The Definition of Ready helps ensure quality backlog items.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Only a title", "is_correct": False},
            {"text": "Clear acceptance criteria and sufficient detail", "is_correct": True},
            {"text": "Technical specifications only", "is_correct": False},
            {"text": "Just the business value", "is_correct": False}
        ]
    },
    {
        "text": "During which event does the Product Owner participate to inspect and adapt the product?",
        "explanation": "The Sprint Review is the event where the Scrum Team and stakeholders inspect the increment and adapt the Product Backlog if needed. The Product Owner actively participates to gather feedback.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Daily Scrum", "is_correct": False},
            {"text": "Sprint Review", "is_correct": True},
            {"text": "Sprint Planning", "is_correct": False},
            {"text": "Sprint Retrospective", "is_correct": False}
        ]
    },
    {
        "text": "What is a key characteristic of a good user story?",
        "explanation": "Good user stories follow the INVEST criteria: Independent, Negotiable, Valuable, Estimable, Small, and Testable. They should provide value to the user and be small enough to complete in a Sprint.",
        "reference": "https://www.agilealliance.org/glossary/user-stories/",
        "points": 1,
        "answers": [
            {"text": "Very detailed technical specifications", "is_correct": False},
            {"text": "Independent, valuable, and estimable", "is_correct": True},
            {"text": "Written only by developers", "is_correct": False},
            {"text": "Never changes once written", "is_correct": False}
        ]
    }
]
