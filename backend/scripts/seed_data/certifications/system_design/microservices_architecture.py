"""Microservices Architecture Certification"""

CERTIFICATION = {
    "name": "Microservices Architecture Professional",
    "description": "Advanced microservices design patterns and implementation",
    "slug": "microservices-architecture-professional",
    "level": "Professional",
    "duration": 150,
    "questions_count": 60,
    "category_slug": "system-design",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the Circuit Breaker pattern in microservices?",
        "explanation": "The Circuit Breaker pattern prevents cascading failures by monitoring service calls and failing fast when a service is unresponsive.",
        "reference": "https://martinfowler.com/bliki/CircuitBreaker.html",
        "points": 1,
        "answers": [
            {"text": "A pattern for load balancing", "is_correct": False},
            {"text": "A pattern to prevent cascading failures", "is_correct": True},
            {"text": "A pattern for data consistency", "is_correct": False},
            {"text": "A pattern for service discovery", "is_correct": False}
        ]
    }
]
