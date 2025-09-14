"""Certified Scrum Product Owner (CSPO) Certification"""

CERTIFICATION = {
    "name": "Certified Scrum Product Owner (CSPO)",
    "description": "Demonstrates expertise in product ownership and value maximization in Scrum teams",
    "slug": "certified-scrum-product-owner-cspo",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "project-management",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the key accountability of a Product Owner according to the Scrum Guide?",
        "explanation": "The Product Owner is accountable for maximizing the value of the product resulting from the work of the Scrum Team. This is achieved through effective Product Backlog management.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Managing the Development Team", "is_correct": False},
            {"text": "Maximizing the value of the product", "is_correct": True},
            {"text": "Facilitating Scrum events", "is_correct": False},
            {"text": "Writing technical documentation", "is_correct": False},
        ],
    },
    {
        "text": "Who can change the priority of items in the Product Backlog?",
        "explanation": "Only the Product Owner has the authority to change the priority of Product Backlog items. While they may listen to input from stakeholders and the team, the final decision rests with the Product Owner.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Any stakeholder", "is_correct": False},
            {"text": "Product Owner only", "is_correct": True},
            {"text": "Scrum Master", "is_correct": False},
            {"text": "Development Team", "is_correct": False},
        ],
    },
    {
        "text": "What happens if the Product Owner is not available during a Sprint?",
        "explanation": "The Product Owner should be available to the Development Team throughout the Sprint to answer questions and provide clarification. If unavailable, it can significantly impact the team's ability to deliver value.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Sprint continues normally", "is_correct": False},
            {"text": "May impact team's ability to deliver value", "is_correct": True},
            {"text": "Scrum Master takes over", "is_correct": False},
            {"text": "Sprint is automatically cancelled", "is_correct": False},
        ],
    },
    {
        "text": "What is the relationship between the Product Owner and stakeholders?",
        "explanation": "The Product Owner represents the stakeholders to the Scrum Team and is responsible for gathering requirements, feedback, and ensuring stakeholder needs are reflected in the Product Backlog.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "No direct relationship", "is_correct": False},
            {"text": "Represents stakeholders to the Scrum Team", "is_correct": True},
            {"text": "Stakeholders manage the Product Owner", "is_correct": False},
            {"text": "Equal partnership with no hierarchy", "is_correct": False},
        ],
    },
    {
        "text": "When should Product Backlog refinement occur?",
        "explanation": "Product Backlog refinement is an ongoing activity throughout the Sprint. The Scrum Team collaborates to add detail, estimates, and order to Product Backlog items as needed.",
        "reference": "https://scrumguides.org/scrum-guide.html",
        "points": 1,
        "answers": [
            {"text": "Only during Sprint Planning", "is_correct": False},
            {"text": "Ongoing throughout the Sprint", "is_correct": True},
            {"text": "Only at Sprint Review", "is_correct": False},
            {"text": "Once per Sprint maximum", "is_correct": False},
        ],
    },
]
