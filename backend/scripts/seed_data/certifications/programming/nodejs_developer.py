"""Node.js Developer Certification"""

CERTIFICATION = {
    "name": "Node.js Developer Certification",
    "description": "Server-side JavaScript with Node.js",
    "slug": "nodejs-developer-certification",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Node.js?",
        "explanation": "Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine that allows you to run JavaScript on the server-side, enabling full-stack JavaScript development.",
        "reference": "https://nodejs.org/en/about/",
        "points": 1,
        "answers": [
            {"text": "A JavaScript framework", "is_correct": False},
            {"text": "A JavaScript runtime environment", "is_correct": True},
            {"text": "A database management system", "is_correct": False},
            {"text": "A CSS preprocessor", "is_correct": False},
        ],
    },
    {
        "text": "What is npm in the Node.js ecosystem?",
        "explanation": "npm (Node Package Manager) is the default package manager for Node.js that allows you to install, manage, and share JavaScript packages and dependencies.",
        "reference": "https://docs.npmjs.com/about-npm",
        "points": 1,
        "answers": [
            {"text": "A debugging tool", "is_correct": False},
            {"text": "A package manager for JavaScript", "is_correct": True},
            {"text": "A testing framework", "is_correct": False},
            {"text": "A web server", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the require() function in Node.js?",
        "explanation": "The require() function is used to import modules, JSON files, and local files in Node.js applications. It follows the CommonJS module system.",
        "reference": "https://nodejs.org/api/modules.html",
        "points": 1,
        "answers": [
            {"text": "To create HTTP servers", "is_correct": False},
            {"text": "To import modules and files", "is_correct": True},
            {"text": "To handle asynchronous operations", "is_correct": False},
            {"text": "To manage memory allocation", "is_correct": False},
        ],
    },
    {
        "text": "What is Express.js?",
        "explanation": "Express.js is a minimal and flexible Node.js web application framework that provides a robust set of features for building web and mobile applications and APIs.",
        "reference": "https://expressjs.com/",
        "points": 1,
        "answers": [
            {"text": "A database ORM", "is_correct": False},
            {"text": "A web application framework for Node.js", "is_correct": True},
            {"text": "A frontend JavaScript library", "is_correct": False},
            {"text": "A CSS framework", "is_correct": False},
        ],
    },
    {
        "text": "What is the event loop in Node.js?",
        "explanation": "The event loop is what allows Node.js to perform non-blocking I/O operations by offloading operations to the system kernel whenever possible, making Node.js single-threaded but highly concurrent.",
        "reference": "https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/",
        "points": 1,
        "answers": [
            {"text": "A debugging mechanism", "is_correct": False},
            {
                "text": "A mechanism for handling asynchronous operations",
                "is_correct": True,
            },
            {"text": "A security feature", "is_correct": False},
            {"text": "A package management system", "is_correct": False},
        ],
    },
]
