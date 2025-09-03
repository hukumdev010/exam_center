"""Advanced Algorithms Certification"""

CERTIFICATION = {
    "name": "Advanced Algorithms",
    "description": "Advanced algorithmic techniques including dynamic programming, greedy algorithms, and graph algorithms",
    "slug": "advanced-algorithms",
    "level": "Professional",
    "duration": 120,
    "questions_count": 80,
    "category_slug": "data-structures-algorithms",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which algorithm is used to find the shortest path in a weighted graph with no negative edges?",
        "explanation": "Dijkstra's algorithm efficiently finds shortest paths in weighted graphs without negative edge weights.",
        "reference": "https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm",
        "points": 1,
        "answers": [
            {"text": "Breadth-First Search", "is_correct": False},
            {"text": "Depth-First Search", "is_correct": False},
            {"text": "Dijkstra's Algorithm", "is_correct": True},
            {"text": "Bellman-Ford Algorithm", "is_correct": False}
        ]
    },
    {
        "text": "What is the key principle behind dynamic programming?",
        "explanation": "Dynamic programming breaks down complex problems into simpler subproblems and stores their solutions to avoid recomputation.",
        "reference": "https://en.wikipedia.org/wiki/Dynamic_programming",
        "points": 1,
        "answers": [
            {"text": "Divide and conquer", "is_correct": False},
            {"text": "Optimal substructure and overlapping subproblems", "is_correct": True},
            {"text": "Greedy choice property", "is_correct": False},
            {"text": "Backtracking", "is_correct": False}
        ]
    }
]
