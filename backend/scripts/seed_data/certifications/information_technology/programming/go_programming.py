"""Go Programming Certification"""

CERTIFICATION = {
    "name": "Go Programming Certification",
    "description": "Google Go programming language",
    "slug": "go-programming-certification",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is a goroutine in Go?",
        "explanation": "A goroutine is a lightweight thread managed by the Go runtime. Goroutines are created using the 'go' keyword and enable concurrent execution of functions.",
        "reference": "https://golang.org/doc/effective_go.html#goroutines",
        "points": 1,
        "answers": [
            {"text": "A Go package", "is_correct": False},
            {"text": "A lightweight thread for concurrency", "is_correct": True},
            {"text": "A data structure", "is_correct": False},
            {"text": "A Go compiler option", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword is used to create a channel in Go?",
        "explanation": "The 'make' keyword is used to create channels in Go. Channels are typed conduits through which you can send and receive values with the channel operator '<-'.",
        "reference": "https://golang.org/doc/effective_go.html#channels",
        "points": 1,
        "answers": [
            {"text": "new", "is_correct": False},
            {"text": "make", "is_correct": True},
            {"text": "create", "is_correct": False},
            {"text": "channel", "is_correct": False},
        ],
    },
    {
        "text": "What is the zero value of a pointer in Go?",
        "explanation": "The zero value of a pointer in Go is nil. This means uninitialized pointers have the value nil and don't point to any memory location.",
        "reference": "https://golang.org/ref/spec#The_zero_value",
        "points": 1,
        "answers": [
            {"text": "0", "is_correct": False},
            {"text": "nil", "is_correct": True},
            {"text": "null", "is_correct": False},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which Go statement is used to handle errors?",
        "explanation": "In Go, errors are typically handled using if statements to check if an error is not nil. Go uses explicit error handling rather than exceptions.",
        "reference": "https://golang.org/doc/effective_go.html#errors",
        "points": 1,
        "answers": [
            {"text": "try-catch", "is_correct": False},
            {"text": "if err != nil", "is_correct": True},
            {"text": "throw", "is_correct": False},
            {"text": "except", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the defer statement in Go?",
        "explanation": "The defer statement defers the execution of a function until the surrounding function returns. Deferred function calls are pushed onto a stack and executed in LIFO order.",
        "reference": "https://golang.org/doc/effective_go.html#defer",
        "points": 1,
        "answers": [
            {"text": "To delay variable declaration", "is_correct": False},
            {
                "text": "To defer function execution until function returns",
                "is_correct": True,
            },
            {"text": "To create asynchronous functions", "is_correct": False},
            {"text": "To optimize performance", "is_correct": False},
        ],
    },
]
