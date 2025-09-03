"""Algorithms Fundamentals Certification"""

CERTIFICATION = {
    "name": "Algorithms Fundamentals",
    "description": "Core algorithms including sorting, searching, recursion, and basic algorithmic techniques",
    "slug": "algorithms-fundamentals",
    "level": "Associate",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "data-structures-algorithms",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the average time complexity of Quick Sort?",
        "explanation": "Quick Sort has an average time complexity of O(n log n), though its worst case is O(n²).",
        "reference": "https://en.wikipedia.org/wiki/Quicksort",
        "points": 1,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(log n)", "is_correct": False}
        ]
    },
    {
        "text": "Which sorting algorithm is stable and has O(n log n) guaranteed time complexity?",
        "explanation": "Merge Sort is stable (maintains relative order of equal elements) and has guaranteed O(n log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Merge_sort",
        "points": 1,
        "answers": [
            {"text": "Quick Sort", "is_correct": False},
            {"text": "Heap Sort", "is_correct": False},
            {"text": "Merge Sort", "is_correct": True},
            {"text": "Selection Sort", "is_correct": False}
        ]
    },
    {
        "text": "What is the time complexity of binary search on a sorted array?",
        "explanation": "Binary search divides the search space in half with each comparison, resulting in O(log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Binary_search_algorithm",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False}
        ]
    }
]
