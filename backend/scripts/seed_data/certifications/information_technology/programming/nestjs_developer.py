"""NestJS Developer Certification"""

CERTIFICATION = {
    "name": "NestJS Developer",
    "description": "NestJS Backend Framework Developer Certification",
    "slug": "nestjs-developer",
    "level": "Intermediate",
    "duration": 8,
    "questions_count": 10,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is NestJS primarily used for?",
        "explanation": "NestJS is a progressive Node.js framework for building efficient and scalable server-side applications, especially APIs and backend services.",
        "reference": "https://docs.nestjs.com/",
        "points": 1,
        "answers": [
            {"text": "Building mobile apps", "is_correct": False},
            {"text": "Building server-side applications", "is_correct": True},
            {"text": "Designing databases", "is_correct": False},
            {"text": "Creating CSS styles", "is_correct": False},
        ],
    },
    {
        "text": "Which default HTTP platform does NestJS commonly use?",
        "explanation": "NestJS uses Express by default, though it can also be configured to use Fastify.",
        "reference": "https://docs.nestjs.com/faq/http-adapter",
        "points": 1,
        "answers": [
            {"text": "Koa", "is_correct": False},
            {"text": "Hapi", "is_correct": False},
            {"text": "Express", "is_correct": True},
            {"text": "Flask", "is_correct": False},
        ],
    },
    {
        "text": "What decorator is used to define a controller in NestJS?",
        "explanation": "The @Controller() decorator marks a class as a NestJS controller that handles incoming requests and returns responses.",
        "reference": "https://docs.nestjs.com/controllers",
        "points": 1,
        "answers": [
            {"text": "@Service()", "is_correct": False},
            {"text": "@Controller()", "is_correct": True},
            {"text": "@Injectable()", "is_correct": False},
            {"text": "@Module()", "is_correct": False},
        ],
    },
    {
        "text": "Which decorator is used to define a provider/service class in NestJS?",
        "explanation": "@Injectable() marks a class as a provider that can be managed and injected by NestJS dependency injection system.",
        "reference": "https://docs.nestjs.com/providers",
        "points": 1,
        "answers": [
            {"text": "@Controller()", "is_correct": False},
            {"text": "@Route()", "is_correct": False},
            {"text": "@Injectable()", "is_correct": True},
            {"text": "@Pipe()", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of a NestJS module?",
        "explanation": "A module organizes related components such as controllers and providers and defines the application structure.",
        "reference": "https://docs.nestjs.com/modules",
        "points": 1,
        "answers": [
            {
                "text": "To style frontend components",
                "is_correct": False,
            },
            {
                "text": "To group related controllers and providers",
                "is_correct": True,
            },
            {"text": "To define SQL schema only", "is_correct": False},
            {"text": "To replace TypeScript", "is_correct": False},
        ],
    },
    {
        "text": "What does dependency injection provide in NestJS?",
        "explanation": "Dependency injection lets NestJS create and supply class dependencies automatically, improving testability and maintainability.",
        "reference": "https://docs.nestjs.com/fundamentals/custom-providers",
        "points": 1,
        "answers": [
            {"text": "Automatic CSS generation", "is_correct": False},
            {
                "text": "Automatic creation and injection of dependencies",
                "is_correct": True,
            },
            {"text": "Automatic database indexing", "is_correct": False},
            {"text": "Automatic code minification", "is_correct": False},
        ],
    },
    {
        "text": "Which NestJS feature is commonly used for request validation?",
        "explanation": "ValidationPipe is commonly used with class-validator/class-transformer to validate incoming request data.",
        "reference": "https://docs.nestjs.com/techniques/validation",
        "points": 1,
        "answers": [
            {"text": "Guard", "is_correct": False},
            {"text": "Interceptor", "is_correct": False},
            {"text": "ValidationPipe", "is_correct": True},
            {"text": "Middleware", "is_correct": False},
        ],
    },
    {
        "text": "What is the role of guards in NestJS?",
        "explanation": "Guards determine whether a request should be handled by the route handler, commonly for authentication and authorization checks.",
        "reference": "https://docs.nestjs.com/guards",
        "points": 1,
        "answers": [
            {"text": "Transform response data", "is_correct": False},
            {
                "text": "Control access to route handlers",
                "is_correct": True,
            },
            {"text": "Handle database migrations", "is_correct": False},
            {"text": "Define DTO classes", "is_correct": False},
        ],
    },
    {
        "text": "Which command is typically used to create a new NestJS project?",
        "explanation": "The Nest CLI command 'nest new' scaffolds a new NestJS project with recommended structure.",
        "reference": "https://docs.nestjs.com/cli/overview",
        "points": 1,
        "answers": [
            {"text": "npm create nest-app", "is_correct": False},
            {"text": "nest new", "is_correct": True},
            {"text": "nest init", "is_correct": False},
            {"text": "node nest new", "is_correct": False},
        ],
    },
    {
        "text": "What is a DTO in NestJS?",
        "explanation": "A DTO (Data Transfer Object) defines the shape of data sent over the network and is often used with validation in NestJS.",
        "reference": "https://docs.nestjs.com/controllers#request-payloads",
        "points": 1,
        "answers": [
            {"text": "Database Transaction Object", "is_correct": False},
            {
                "text": "Data Transfer Object",
                "is_correct": True,
            },
            {"text": "Dynamic Type Operation", "is_correct": False},
            {"text": "Default Template Option", "is_correct": False},
        ],
    },
]
