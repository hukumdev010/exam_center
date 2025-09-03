"""High-Performance System Architecture Certification"""

CERTIFICATION = {
    "name": "High-Performance System Architecture",
    "description": "Designing and implementing high-performance, scalable systems",
    "slug": "high-performance-system-architecture",
    "level": "Expert",
    "duration": 180,
    "questions_count": 75,
    "category_slug": "system-design",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the primary benefit of using a Content Delivery Network (CDN)?",
        "explanation": "CDNs reduce latency by serving content from geographically distributed edge locations closer to users.",
        "reference": "https://en.wikipedia.org/wiki/Content_delivery_network",
        "points": 1,
        "answers": [
            {"text": "Increased security", "is_correct": False},
            {"text": "Reduced latency and improved performance", "is_correct": True},
            {"text": "Better SEO rankings", "is_correct": False},
            {"text": "Lower storage costs", "is_correct": False}
        ]
    }
]
