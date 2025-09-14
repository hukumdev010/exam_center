"""TypeScript Developer Certification"""

CERTIFICATION = {
    "name": "TypeScript Developer Certification",
    "description": "TypeScript language features, type system, and advanced programming concepts",
    "slug": "typescript-developer-certification",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the main benefit of using TypeScript over JavaScript?",
        "explanation": "TypeScript adds static type checking to JavaScript, helping catch errors at compile time rather than runtime.",
        "reference": "https://www.typescriptlang.org/docs/",
        "points": 1,
        "answers": [
            {"text": "Faster runtime performance", "is_correct": False},
            {"text": "Static type checking", "is_correct": True},
            {"text": "Smaller bundle size", "is_correct": False},
            {"text": "Built-in testing framework", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript feature allows you to define optional properties in an interface?",
        "explanation": "The question mark (?) syntax allows you to define optional properties in TypeScript interfaces.",
        "reference": "https://www.typescriptlang.org/docs/handbook/2/objects.html",
        "points": 1,
        "answers": [
            {"text": "property?", "is_correct": True},
            {"text": "property | undefined", "is_correct": False},
            {"text": "optional property", "is_correct": False},
            {"text": "property: any", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'never' type represent in TypeScript?",
        "explanation": "The 'never' type represents values that never occur, such as functions that always throw errors or have infinite loops.",
        "reference": "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type",
        "points": 1,
        "answers": [
            {"text": "A type that can be anything", "is_correct": False},
            {"text": "A type that represents null or undefined", "is_correct": False},
            {"text": "A type for values that never occur", "is_correct": True},
            {"text": "A type for boolean values", "is_correct": False},
        ],
    },
    {
        "text": "How do you define a generic function in TypeScript?",
        "explanation": "Generic functions in TypeScript are defined using angle brackets with type parameters, like function<T>(param: T): T.",
        "reference": "https://www.typescriptlang.org/docs/handbook/2/generics.html",
        "points": 1,
        "answers": [
            {"text": "function<T>(param: T): T", "is_correct": True},
            {"text": "function(param: generic): generic", "is_correct": False},
            {"text": "generic function(param: T): T", "is_correct": False},
            {"text": "function[T](param: T): T", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the 'readonly' modifier in TypeScript?",
        "explanation": "The 'readonly' modifier prevents modification of a property after initialization, making it immutable.",
        "reference": "https://www.typescriptlang.org/docs/handbook/2/classes.html#readonly",
        "points": 1,
        "answers": [
            {"text": "Makes properties private", "is_correct": False},
            {"text": "Prevents modification after initialization", "is_correct": True},
            {"text": "Makes properties optional", "is_correct": False},
            {"text": "Allows null values", "is_correct": False},
        ],
    },
]
