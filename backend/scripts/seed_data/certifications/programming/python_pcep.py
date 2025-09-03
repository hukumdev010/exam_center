"""Python Institute PCEP Certification"""

CERTIFICATION = {
    "name": "Python Institute PCEP",
    "description": "Python Certified Entry-Level Programmer",
    "slug": "python-pcep",
    "level": "Entry",
    "duration": 65,
    "questions_count": 30,
    "category_slug": "programming",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which of the following is a mutable data type in Python?",
        "explanation": "Lists are mutable in Python, meaning their contents can be changed after creation.",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html",
        "points": 1,
        "answers": [
            {"text": "tuple", "is_correct": False},
            {"text": "string", "is_correct": False},
            {"text": "list", "is_correct": True},
            {"text": "frozenset", "is_correct": False}
        ]
    },
    {
        "text": "What is the output of print(type(5.0))?",
        "explanation": "5.0 is a floating-point number, so its type is <class 'float'>.",
        "reference": "https://docs.python.org/3/library/functions.html#type",
        "points": 1,
        "answers": [
            {"text": "<class 'int'>", "is_correct": False},
            {"text": "<class 'float'>", "is_correct": True},
            {"text": "<class 'number'>", "is_correct": False},
            {"text": "<class 'decimal'>", "is_correct": False}
        ]
    }
]
