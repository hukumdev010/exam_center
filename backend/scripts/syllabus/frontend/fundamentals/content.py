"""Syllabus content for Frontend with React - Fundamentals (seed)

This file exports SYLLABUS_JSON which is a JSON string consumed by the
existing seeding machinery. Keeping the content as a JSON string preserves
the existing behavior (the Certification.syllabus column expects text).
"""

"""
Note: Detailed content for topics is loaded dynamically from the topics/ 
directory by the SyllabusService. This allows us to keep the detailed 
content in separate, maintainable files while preserving the existing 
seeding process.
"""

SYLLABUS_JSON = """{
        "courseOverview": {
            "title": "Frontend Development - Full Stack",
            "description": "A comprehensive course covering all aspects of modern frontend development including web fundamentals, JavaScript, HTML/CSS, design systems, responsive design, performance optimization, and advanced frameworks like React for building scalable web applications",
            "duration": "14-16 weeks",
            "difficulty": "Beginner to Advanced",
            "prerequisites": ["Basic computer literacy", "Familiarity with web browsers", "Text editor knowledge"]
        },
        "modules": [
            {
                "moduleNumber": 1,
                "title": "Web Development Fundamentals",
                "duration": "Week 1",
                "topics": [
                    "What is Web Development",
                    "Frontend vs Backend vs Fullstack",
                    "Client-Server Architecture",
                    "Web Browser Overview",
                    "Developer Tools and DevTools",
                    "Code Editors and IDEs",
                    "Command Line Basics",
                    "Git and Version Control",
                    "Project Initialization",
                    "Localhost and Local Development",
                    "Production vs Development",
                    "Web Standards and W3C",
                    "Browser Compatibility",
                    "Performance Considerations",
                    "Accessibility Basics"
                ],
                "learningObjectives": [
                    "Understand web development fundamentals",
                    "Set up development environment",
                    "Learn essential tools"
                ]
            },
            {
                "moduleNumber": 2,
                "title": "HTML5 Fundamentals",
                "duration": "Week 1-2",
                "topics": [
                    "HTML Structure and Syntax",
                    "HTML Document Structure",
                    "Semantic HTML Elements",
                    "Text Formatting Elements",
                    "Links and Navigation",
                    "Images and Media",
                    "Lists (Ordered, Unordered, Description)",
                    "Tables and Data",
                    "Forms and Input Elements",
                    "Form Attributes and Validation",
                    "Input Types",
                    "Labels and Accessibility",
                    "Meta Tags",
                    "SEO Meta Tags",
                    "Open Graph Tags",
                    "Favicon and Site Icons",
                    "Attributes and Data Attributes",
                    "HTML Best Practices",
                    "Validation and Testing"
                ],
                "learningObjectives": [
                    "Master HTML5 semantics",
                    "Create accessible forms",
                    "Understand HTML structure"
                ]
            },
            {
                "moduleNumber": 3,
                "title": "CSS Fundamentals & Layout",
                "duration": "Week 2-3",
                "topics": [
                    "CSS Syntax and Selectors",
                    "Element Selectors",
                    "Class and ID Selectors",
                    "Pseudo-classes and Pseudo-elements",
                    "Attribute Selectors",
                    "Combinators",
                    "CSS Specificity",
                    "Cascading and Inheritance",
                    "Colors and Backgrounds",
                    "Typography and Fonts",
                    "Font Families and Google Fonts",
                    "Box Model (Margin, Padding, Border)",
                    "Display Property (Block, Inline, Inline-Block)",
                    "Position Property",
                    "Z-index and Layering",
                    "Flexbox Layout",
                    "CSS Grid Layout",
                    "Alignment and Centering",
                    "Overflow and Clipping"
                ],
                "learningObjectives": [
                    "Master CSS fundamentals",
                    "Understand layout systems",
                    "Create flexible designs"
                ]
            },
            {
                "moduleNumber": 4,
                "title": "Advanced CSS & Responsive Design",
                "duration": "Week 3-4",
                "topics": [
                    "CSS Transitions",
                    "CSS Animations",
                    "Keyframes",
                    "Transform Property",
                    "Gradients (Linear, Radial)",
                    "Box Shadows and Text Shadows",
                    "CSS Filters",
                    "Media Queries",
                    "Responsive Design Principles",
                    "Mobile-First Approach",
                    "Breakpoints Strategy",
                    "Fluid Typography",
                    "Relative Units (em, rem, vh, vw)",
                    "Mobile Navigation Patterns",
                    "Touch-Friendly Interfaces",
                    "Print Styles",
                    "CSS Variables (Custom Properties)",
                    "CSS Preprocessors (Sass/SCSS)",
                    "Mixins and Functions",
                    "CSS Organization and BEM"
                ],
                "learningObjectives": [
                    "Create responsive layouts",
                    "Master animations",
                    "Use CSS preprocessors"
                ]
            },
            {
                "moduleNumber": 5,
                "title": "JavaScript Fundamentals & ES6+",
                "duration": "Week 4-5",
                "topics": [
                    "Variables and Data Types",
                    "Operators and Control Flow",
                    "Functions and Scope",
                    "Arrow Functions",
                    "Destructuring",
                    "Spread Operator",
                    "Template Literals",
                    "Let, Const, and Var",
                    "Closures",
                    "Callbacks and Higher-Order Functions",
                    "Promises",
                    "Async/Await",
                    "Error Handling",
                    "Regular Expressions",
                    "Object Methods",
                    "Array Methods (map, filter, reduce, etc.)",
                    "Rest Parameters",
                    "Default Parameters",
                    "Modules and Imports/Exports"
                ],
                "learningObjectives": [
                    "Master JavaScript fundamentals",
                    "Understand ES6+ syntax and features",
                    "Handle asynchronous operations effectively"
                ]
            },
            {
                "moduleNumber": 6,
                "title": "DOM Manipulation & APIs",
                "duration": "Week 5-6",
                "topics": [
                    "DOM Basics",
                    "Selecting Elements",
                    "querySelector and querySelectorAll",
                    "getElementById and getElementsBy*",
                    "Creating and Removing Elements",
                    "Modifying Element Properties",
                    "innerHTML vs textContent",
                    "Attributes and Properties",
                    "Event Listeners",
                    "Event Handling",
                    "Event Bubbling and Capturing",
                    "Delegated Events",
                    "Event Object",
                    "classList Methods",
                    "style Property",
                    "Data Attributes",
                    "Window Object",
                    "Document Object",
                    "LocalStorage and SessionStorage",
                    "Cookies Management"
                ],
                "learningObjectives": [
                    "Manipulate the DOM",
                    "Handle events efficiently",
                    "Work with browser APIs"
                ]
            },
            {
                "moduleNumber": 7,
                "title": "Asynchronous JavaScript",
                "duration": "Week 6",
                "topics": [
                    "Callbacks",
                    "Callback Hell",
                    "Promises",
                    "Promise Creation",
                    "Promise States",
                    "then() and catch()",
                    "Promise.all() and Promise.race()",
                    "Async/Await Syntax",
                    "Error Handling in Async",
                    "Try-Catch-Finally",
                    "setTimeout and setInterval",
                    "requestAnimationFrame",
                    "Microtasks vs Macrotasks",
                    "Event Loop",
                    "Call Stack",
                    "Task Queue",
                    "Debugging Async Code",
                    "Promise Chaining",
                    "Concurrent vs Sequential Async"
                ],
                "learningObjectives": [
                    "Master asynchronous patterns",
                    "Handle callbacks effectively",
                    "Use async/await"
                ]
            },
            {
                "moduleNumber": 8,
                "title": "API Integration & Data Fetching",
                "duration": "Week 6-7",
                "topics": [
                    "Fetch API",
                    "HTTP Methods",
                    "Request Headers",
                    "Response Handling",
                    "JSON Parsing",
                    "Query Parameters",
                    "Request Body",
                    "CORS and CORS Errors",
                    "Error Handling",
                    "Status Codes",
                    "Axios Library",
                    "Request Interceptors",
                    "Response Interceptors",
                    "Request Timeout",
                    "Request Cancellation",
                    "FormData Submission",
                    "File Upload",
                    "Blob and Stream Handling",
                    "API Rate Limiting"
                ],
                "learningObjectives": [
                    "Fetch data from APIs",
                    "Handle responses and errors",
                    "Work with different content types"
                ]
            },
            {
                "moduleNumber": 9,
                "title": "Object-Oriented JavaScript",
                "duration": "Week 7",
                "topics": [
                    "Objects and Objects Literals",
                    "Constructor Functions",
                    "Prototypes",
                    "Prototype Chain",
                    "Classes",
                    "Class Constructors",
                    "Instance and Static Methods",
                    "Inheritance",
                    "super Keyword",
                    "Getters and Setters",
                    "this Keyword",
                    "Bind, Call, Apply",
                    "Encapsulation",
                    "Private Fields",
                    "Factory Functions",
                    "Singleton Pattern",
                    "Module Pattern",
                    "Design Patterns"
                ],
                "learningObjectives": [
                    "Understand OOP principles",
                    "Master prototypal inheritance",
                    "Use design patterns"
                ]
            },
            {
                "moduleNumber": 10,
                "title": "Functional JavaScript",
                "duration": "Week 7-8",
                "topics": [
                    "First-Class Functions",
                    "Higher-Order Functions",
                    "Arrow Functions",
                    "Closures",
                    "Pure Functions",
                    "Function Composition",
                    "Currying",
                    "Partial Application",
                    "Map, Filter, Reduce",
                    "Array Methods",
                    "Immutability",
                    "Destructuring Objects",
                    "Destructuring Arrays",
                    "Spread Operator",
                    "Rest Parameters",
                    "Recursion",
                    "Tail Call Optimization",
                    "Functional Libraries (Lodash, Ramda)"
                ],
                "learningObjectives": [
                    "Master functional programming",
                    "Use functional methods",
                    "Understand immutability"
                ]
            },
            {
                "moduleNumber": 11,
                "title": "Error Handling & Debugging",
                "duration": "Week 8",
                "topics": [
                    "Error Types",
                    "Syntax Errors",
                    "Runtime Errors",
                    "Logic Errors",
                    "Try-Catch-Finally",
                    "Throw Statement",
                    "Custom Errors",
                    "Error Stack Traces",
                    "Console Methods",
                    "Debugger Statement",
                    "Browser DevTools Debugger",
                    "Breakpoints",
                    "Step Through Code",
                    "Watch Expressions",
                    "Call Stack Analysis",
                    "Source Maps",
                    "Performance Analysis",
                    "Memory Leaks Detection"
                ],
                "learningObjectives": [
                    "Handle errors effectively",
                    "Debug code efficiently",
                    "Use developer tools"
                ]
            },
            {
                "moduleNumber": 12,
                "title": "Modules and Build Systems",
                "duration": "Week 8",
                "topics": [
                    "Module Systems",
                    "CommonJS",
                    "ES6 Modules",
                    "Import/Export",
                    "npm and Package Management",
                    "package.json",
                    "Dependencies vs DevDependencies",
                    "Semantic Versioning",
                    "Webpack Basics",
                    "Bundling",
                    "Loaders",
                    "Plugins",
                    "Vite",
                    "Rollup",
                    "Code Splitting",
                    "Tree Shaking",
                    "Build Configuration",
                    "Production vs Development Builds"
                ],
                "learningObjectives": [
                    "Manage dependencies",
                    "Understand modules",
                    "Configure build tools"
                ]
            },
            {
                "moduleNumber": 13,
                "title": "Web APIs & Browser Features",
                "duration": "Week 9",
                "topics": [
                    "Geolocation API",
                    "Web Audio API",
                    "Canvas API",
                    "SVG",
                    "WebGL",
                    "Service Workers",
                    "Web Workers",
                    "Fetch API Advanced",
                    "Notification API",
                    "Permission API",
                    "Payment Request API",
                    "Sensor APIs",
                    "Vibration API",
                    "Battery Status API",
                    "Network Information API",
                    "Screen Orientation API",
                    "Local Storage",
                    "IndexedDB",
                    "WebSockets"
                ],
                "learningObjectives": [
                    "Explore modern browser APIs",
                    "Build advanced features",
                    "Improve user experience"
                ]
            },
            {
                "moduleNumber": 14,
                "title": "Performance & Optimization",
                "duration": "Week 9",
                "topics": [
                    "Web Vitals",
                    "Lighthouse Audits",
                    "Performance Metrics",
                    "Page Load Speed",
                    "Image Optimization",
                    "Lazy Loading",
                    "Code Splitting",
                    "Tree Shaking",
                    "Minification and Compression",
                    "Caching Strategies",
                    "CDN Usage",
                    "Bundle Analysis",
                    "CSS Optimization",
                    "JavaScript Optimization",
                    "Resource Hints",
                    "Preload and Prefetch",
                    "Rendering Performance",
                    "Paint and Layout Thrashing"
                ],
                "learningObjectives": [
                    "Optimize web performance",
                    "Measure performance metrics",
                    "Improve user experience"
                ]
            },
            {
                "moduleNumber": 15,
                "title": "Accessibility & SEO",
                "duration": "Week 9-10",
                "topics": [
                    "Accessibility Principles (WCAG)",
                    "Semantic HTML for Accessibility",
                    "ARIA Attributes",
                    "Keyboard Navigation",
                    "Screen Readers",
                    "Color Contrast",
                    "Focus Management",
                    "Form Accessibility",
                    "Image Alt Text",
                    "Video Accessibility",
                    "Captions and Transcripts",
                    "Testing Accessibility",
                    "SEO Fundamentals",
                    "Meta Tags",
                    "Structured Data",
                    "Schema Markup",
                    "Open Graph Tags",
                    "Robots.txt",
                    "XML Sitemaps"
                ],
                "learningObjectives": [
                    "Build accessible websites",
                    "Optimize for SEO",
                    "Ensure inclusive design"
                ]
            },
            {
                "moduleNumber": 16,
                "title": "Design Systems & UI Libraries",
                "duration": "Week 10",
                "topics": [
                    "Design System Principles",
                    "Component Libraries",
                    "Bootstrap",
                    "Tailwind CSS",
                    "Material Design",
                    "Material-UI (MUI)",
                    "Ant Design",
                    "Chakra UI",
                    "Semantic UI",
                    "Foundation",
                    "Theme Customization",
                    "Dark Mode Implementation",
                    "Design Tokens",
                    "Icon Systems",
                    "Typography Systems",
                    "Color Palettes",
                    "Component Documentation",
                    "Storybook"
                ],
                "learningObjectives": [
                    "Use UI component libraries",
                    "Customize themes",
                    "Create consistent designs"
                ]
            },
            {
                "moduleNumber": 17,
                "title": "Testing and Quality Assurance",
                "duration": "Week 10-11",
                "topics": [
                    "Testing Principles",
                    "Unit Testing",
                    "Integration Testing",
                    "End-to-End Testing",
                    "Jest Framework",
                    "Mocha",
                    "Chai Assertions",
                    "Cypress",
                    "Puppeteer",
                    "Test Coverage",
                    "Mocking Functions",
                    "Spies",
                    "Stubs",
                    "Fixtures",
                    "Test-Driven Development (TDD)",
                    "Behavior-Driven Development (BDD)",
                    "Continuous Testing",
                    "Code Quality Tools"
                ],
                "learningObjectives": [
                    "Write effective tests",
                    "Ensure code quality",
                    "Implement testing strategies"
                ]
            },
            {
                "moduleNumber": 18,
                "title": "Version Control & Collaboration",
                "duration": "Week 11",
                "topics": [
                    "Git Basics",
                    "Repository Management",
                    "Branches",
                    "Commits",
                    "Push and Pull",
                    "Merge and Rebase",
                    "Conflict Resolution",
                    "Stashing",
                    "GitHub",
                    "GitLab",
                    "Pull Requests",
                    "Code Review",
                    "Collaboration Workflows",
                    "Fork and Clone",
                    "Contributing to Open Source",
                    "GitHub Pages",
                    "GitHub Actions",
                    "CI/CD Pipeline"
                ],
                "learningObjectives": [
                    "Master version control",
                    "Collaborate effectively",
                    "Automate workflows"
                ]
            },
            {
                "moduleNumber": 19,
                "title": "React Fundamentals",
                "duration": "Week 11-12",
                "topics": [
                    "What is React",
                    "Virtual DOM",
                    "React Reconciliation",
                    "Functional Components",
                    "Class Components",
                    "JSX Syntax",
                    "Rendering Elements",
                    "Component Composition",
                    "Reusable Components",
                    "React.Fragment",
                    "React DevTools",
                    "Create React App",
                    "Vite Setup",
                    "Props Basics",
                    "State Basics"
                ],
                "learningObjectives": [
                    "Understand React core concepts",
                    "Build functional components",
                    "Master JSX syntax"
                ]
            },
            {
                "moduleNumber": 20,
                "title": "React Frameworks & Metaframeworks",
                "duration": "Week 12-13",
                "topics": [
                    "Next.js Fundamentals",
                    "File-based Routing",
                    "Server-Side Rendering (SSR)",
                    "Static Generation",
                    "API Routes",
                    "Incremental Static Regeneration (ISR)",
                    "App Router vs Pages Router",
                    "Gatsby",
                    "Remix",
                    "Astro",
                    "Framework Selection",
                    "SEO with Frameworks",
                    "Performance with Frameworks",
                    "Deployment Strategies",
                    "Vercel Platform"
                ],
                "learningObjectives": [
                    "Use React metaframeworks",
                    "Implement SSR and SSG",
                    "Deploy React applications"
                ]
            }
        ],
        "practicalProjects": [
            "Personal Portfolio Website",
            "Responsive Blog Platform",
            "E-commerce Product Catalog",
            "Todo List Application with LocalStorage",
            "Weather Dashboard with API Integration",
            "Chat Application with WebSockets",
            "Task Management System",
            "Social Media Feed",
            "Real Estate Marketplace",
            "Project Management Tool",
            "Video Streaming Platform",
            "Music Player Application",
            "Photo Gallery with Lazy Loading",
            "Document Editor",
            "Analytics Dashboard"
        ],
        "assessmentCriteria": [
            "HTML and semantic markup proficiency",
            "CSS layout and responsive design skills",
            "JavaScript fundamentals and ES6+ knowledge",
            "DOM manipulation and event handling",
            "Asynchronous programming capabilities",
            "API integration and data fetching",
            "React component architecture",
            "State management proficiency",
            "Routing and navigation implementation",
            "Performance optimization awareness",
            "Testing and debugging capabilities",
            "Accessibility compliance",
            "SEO implementation",
            "Version control and collaboration",
            "Production-ready code quality"
        ],
        "recommendedReadings": [
            "Eloquent JavaScript by Marijn Haverbeke",
            "JavaScript: The Definitive Guide by David Flanagan",
            "CSS Secrets by Lea Verou",
            "Web Performance in Action by Jeremy Wagner",
            "You Don't Know JS by Kyle Simpson",
            "React Documentation (official)",
            "The Road to React by Robin Wieruch",
            "Learning React by Alex Banks and Eve Porcello",
            "A Book Apart Series on HTML, CSS, and Web Design",
            "MDN Web Docs"
        ],
        "toolsAndTechnologies": [
            "HTML5",
            "CSS3",
            "JavaScript (ES6+)",
            "Browser DevTools",
            "Git and GitHub",
            "Node.js and npm",
            "Webpack/Vite",
            "CSS Preprocessors (Sass/SCSS)",
            "Responsive Design Tools",
            "Flexbox and CSS Grid",
            "SVG and Canvas",
            "Web APIs",
            "Fetch API / Axios",
            "LocalStorage / IndexedDB",
            "Service Workers",
            "Webpack/Vite for bundling",
            "ESLint for linting",
            "Prettier for formatting",
            "Storybook for component documentation",
            "Jest and React Testing Library",
            "Cypress for E2E testing",
            "React 18+",
            "React Router",
            "Redux / Context API",
            "TypeScript",
            "Next.js for SSR",
            "Tailwind CSS / Bootstrap",
            "Material-UI",
            "Web Performance Tools (Lighthouse, WebPageTest)",
            "Docker for containerization",
            "GitHub Actions for CI/CD"
        ]
    }"""
