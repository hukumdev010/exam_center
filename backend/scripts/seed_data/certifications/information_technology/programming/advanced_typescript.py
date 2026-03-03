"""Advanced TypeScript Certification"""

CERTIFICATION = {
    "name": "Advanced TypeScript Certification",
    "description": "Advanced TypeScript concepts including utility types, mapped types, conditional types, and decorators",
    "slug": "advanced-typescript-certification",
    "level": "Professional",
    "duration": 9,
    "questions_count": 3,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does the 'Partial<T>' utility type do in TypeScript?",
        "explanation": "Partial<T> creates a type with all properties of T set to optional, useful for partial updates.",
        "reference": "https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype",
        "points": 1,
        "answers": [
            {"text": "Makes all properties required", "is_correct": False},
            {"text": "Makes all properties optional", "is_correct": True},
            {"text": "Removes all properties", "is_correct": False},
            {"text": "Makes all properties readonly", "is_correct": False},
        ],
    },
    {
        "text": "How do you create a mapped type that makes all properties readonly?",
        "explanation": "The mapped type syntax { readonly [K in keyof T]: T[K] } makes all properties of T readonly.",
        "reference": "https://www.typescriptlang.org/docs/handbook/2/mapped-types.html",
        "points": 1,
        "answers": [
            {"text": "{ readonly [K in keyof T]: T[K] }", "is_correct": True},
            {"text": "{ [K in keyof T]: readonly T[K] }", "is_correct": False},
            {"text": "{ [readonly K in keyof T]: T[K] }", "is_correct": False},
            {"text": "readonly { [K in keyof T]: T[K] }", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of conditional types in TypeScript?",
        "explanation": "Conditional types allow you to choose between two possible types based on a condition, using the ternary operator syntax.",
        "reference": "https://www.typescriptlang.org/docs/handbook/2/conditional-types.html",
        "points": 1,
        "answers": [
            {"text": "To make types optional", "is_correct": False},
            {"text": "To choose between types based on conditions", "is_correct": True},
            {"text": "To create union types", "is_correct": False},
            {"text": "To make types readonly", "is_correct": False},
        ],
    },
]
