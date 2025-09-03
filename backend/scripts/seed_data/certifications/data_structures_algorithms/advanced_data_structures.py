"""Advanced Data Structures Certification"""

CERTIFICATION = {
    "name": "Advanced Data Structures",
    "description": "Advanced data structures including heaps, tries, balanced trees, and graph representations",
    "slug": "advanced-data-structures",
    "level": "Professional",
    "duration": 120,
    "questions_count": 80,
    "category_slug": "data-structures-algorithms",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the time complexity of inserting into a min-heap?",
        "explanation": "Inserting into a heap requires adding the element at the end and bubbling up, which takes O(log n) time.",
        "reference": "https://en.wikipedia.org/wiki/Binary_heap",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False}
        ]
    },
    {
        "text": "Which data structure is most efficient for prefix matching in strings?",
        "explanation": "A Trie (prefix tree) is specifically designed for efficient prefix matching and string operations.",
        "reference": "https://en.wikipedia.org/wiki/Trie",
        "points": 1,
        "answers": [
            {"text": "Hash Table", "is_correct": False},
            {"text": "Binary Search Tree", "is_correct": False},
            {"text": "Trie", "is_correct": True},
            {"text": "Array", "is_correct": False}
        ]
    }
]
