"""Algorithm Design and Analysis Certification"""

CERTIFICATION = {
    "name": "Algorithm Design and Analysis",
    "description": "Comprehensive algorithm design patterns, complexity analysis, and optimization techniques",
    "slug": "algorithm-design-analysis",
    "level": "Expert",
    "duration": 150,
    "questions_count": 100,
    "category_slug": "data-structures-algorithms",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What does Big O notation describe?",
        "explanation": "Big O notation describes the upper bound of an algorithm's time or space complexity in terms of input size.",
        "reference": "https://en.wikipedia.org/wiki/Big_O_notation",
        "points": 1,
        "answers": [
            {"text": "Exact runtime of an algorithm", "is_correct": False},
            {"text": "Upper bound of algorithm complexity", "is_correct": True},
            {"text": "Lower bound of algorithm complexity", "is_correct": False},
            {"text": "Average case complexity", "is_correct": False}
        ]
    },
    {
        "text": "Which approach is most suitable for solving the 0/1 Knapsack problem optimally?",
        "explanation": "Dynamic programming provides an optimal solution for the 0/1 Knapsack problem by building up solutions for smaller capacities.",
        "reference": "https://en.wikipedia.org/wiki/Knapsack_problem",
        "points": 1,
        "answers": [
            {"text": "Greedy algorithm", "is_correct": False},
            {"text": "Brute force", "is_correct": False},
            {"text": "Dynamic programming", "is_correct": True},
            {"text": "Divide and conquer", "is_correct": False}
        ]
    }
]
