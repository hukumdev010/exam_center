"""Data Structures Fundamentals Certification"""

CERTIFICATION = {
    "name": "Data Structures Fundamentals",
    "description": "Core data structures including arrays, linked lists, stacks, queues, trees, and graphs",
    "slug": "data-structures-fundamentals",
    "level": "Associate",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "data-structures-algorithms",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the time complexity of inserting an element at the beginning of a linked list?",
        "explanation": "Inserting at the beginning of a linked list only requires updating the head pointer and the new node's next pointer, which is a constant time operation.",
        "reference": "https://en.wikipedia.org/wiki/Linked_list",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n²)", "is_correct": False}
        ]
    },
    {
        "text": "Which data structure follows LIFO (Last In, First Out) principle?",
        "explanation": "A stack follows the LIFO principle where the last element added is the first one to be removed.",
        "reference": "https://en.wikipedia.org/wiki/Stack_(abstract_data_type)",
        "points": 1,
        "answers": [
            {"text": "Queue", "is_correct": False},
            {"text": "Stack", "is_correct": True},
            {"text": "Array", "is_correct": False},
            {"text": "Hash Table", "is_correct": False}
        ]
    },
    {
        "text": "What is the worst-case time complexity for searching in a binary search tree?",
        "explanation": "In the worst case (when the tree is completely unbalanced), searching in a BST degrades to O(n) where n is the number of nodes.",
        "reference": "https://en.wikipedia.org/wiki/Binary_search_tree",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False}
        ]
    }
]
