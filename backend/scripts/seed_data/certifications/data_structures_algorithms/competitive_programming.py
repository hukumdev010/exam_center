"""Competitive Programming Certification"""

CERTIFICATION = {
    "name": "Competitive Programming",
    "description": "Problem-solving skills for coding competitions and technical interviews",
    "slug": "competitive-programming",
    "level": "Expert",
    "duration": 180,
    "questions_count": 120,
    "category_slug": "data-structures-algorithms",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the time complexity of finding the Longest Common Subsequence using dynamic programming?",
        "explanation": "The LCS problem using DP has a time complexity of O(m*n) where m and n are the lengths of the two sequences.",
        "reference": "https://en.wikipedia.org/wiki/Longest_common_subsequence_problem",
        "points": 1,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(m * n)", "is_correct": True},
            {"text": "O(2^n)", "is_correct": False}
        ]
    },
    {
        "text": "Which technique is most effective for solving problems with optimal substructure?",
        "explanation": "Dynamic programming is ideal for problems that exhibit optimal substructure and overlapping subproblems.",
        "reference": "https://en.wikipedia.org/wiki/Optimal_substructure",
        "points": 1,
        "answers": [
            {"text": "Greedy algorithms", "is_correct": False},
            {"text": "Dynamic programming", "is_correct": True},
            {"text": "Backtracking", "is_correct": False},
            {"text": "Branch and bound", "is_correct": False}
        ]
    }
]
