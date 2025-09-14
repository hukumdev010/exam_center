"""React Developer Certification"""

CERTIFICATION = {
    "name": "React Developer Certification",
    "description": "React.js framework expertise",
    "slug": "react-developer-certification",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is JSX in React?",
        "explanation": "JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code in React components. It gets transpiled to React.createElement() calls.",
        "reference": "https://reactjs.org/docs/introducing-jsx.html",
        "points": 1,
        "answers": [
            {"text": "A CSS preprocessor", "is_correct": False},
            {"text": "A syntax extension for JavaScript", "is_correct": True},
            {"text": "A React library", "is_correct": False},
            {"text": "A database query language", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of React Hooks?",
        "explanation": "React Hooks allow you to use state and other React features in functional components without writing a class component. They provide a way to reuse stateful logic between components.",
        "reference": "https://reactjs.org/docs/hooks-intro.html",
        "points": 1,
        "answers": [
            {"text": "To style components", "is_correct": False},
            {
                "text": "To use state and lifecycle in functional components",
                "is_correct": True,
            },
            {"text": "To handle routing", "is_correct": False},
            {"text": "To manage HTTP requests", "is_correct": False},
        ],
    },
    {
        "text": "What is the Virtual DOM in React?",
        "explanation": "The Virtual DOM is a JavaScript representation of the actual DOM kept in memory. React uses it to optimize updates by comparing the virtual DOM with the previous version and only updating changed elements.",
        "reference": "https://reactjs.org/docs/faq-internals.html",
        "points": 1,
        "answers": [
            {"text": "A real DOM element", "is_correct": False},
            {"text": "A JavaScript representation of the DOM", "is_correct": True},
            {"text": "A CSS framework", "is_correct": False},
            {"text": "A server-side rendering tool", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between props and state in React?",
        "explanation": "Props are read-only data passed down from parent to child components, while state is mutable data managed within a component that can change over time and trigger re-renders.",
        "reference": "https://reactjs.org/docs/components-and-props.html",
        "points": 1,
        "answers": [
            {"text": "Props are mutable, state is immutable", "is_correct": False},
            {
                "text": "Props are passed from parent, state is managed within component",
                "is_correct": True,
            },
            {"text": "Props and state are the same thing", "is_correct": False},
            {"text": "Props are for styling, state is for data", "is_correct": False},
        ],
    },
    {
        "text": "What is the useEffect Hook used for?",
        "explanation": "useEffect is used to perform side effects in functional components, such as data fetching, subscriptions, or manually changing the DOM. It serves the same purpose as componentDidMount, componentDidUpdate, and componentWillUnmount combined.",
        "reference": "https://reactjs.org/docs/hooks-effect.html",
        "points": 1,
        "answers": [
            {"text": "To manage component state", "is_correct": False},
            {
                "text": "To perform side effects and lifecycle operations",
                "is_correct": True,
            },
            {"text": "To handle form validation", "is_correct": False},
            {"text": "To create custom components", "is_correct": False},
        ],
    },
]
