"""
Project Initialization - Detailed Content

This file contains content for the "Project Initialization" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Project Initialization",
    "duration": "10-15 minutes",
    "difficulty": "Beginner",
    "overview": """
    Starting a new web development project involves setting up the correct folder structure, configuration files,
    and dependencies. This topic covers best practices for initializing both simple static projects and Node.js/npm
    projects, ensuring a solid foundation for your work.
    """,
    
    "detailed_content": {
        "introduction": """
Before you write a single line of code, you need to set up your project properly. A well-initialized project has:

- Clear folder structure
- Configuration files (package.json, .gitignore, etc.)
- Proper dependencies installed
- Git repository initialized
- Clear README documentation

Taking time to set up your project correctly saves enormous amounts of time later and makes collaboration easier.
Many beginners skip this step, but professional developers always start with a solid foundation.

There are different approaches depending on your project type: a simple static HTML site, a Node.js project, or
a React application. Let's cover all of them.
        """,
        
        "key_concepts": {
            "project_structure": """
**Why Structure Matters**

Good structure means:
- Easy to find files
- Clear organization
- Scales as project grows
- Team members understand it instantly
- Build tools know where to find files

**Basic Static Project Structure**

For a simple HTML/CSS/JavaScript project:

```
my-website/
├── index.html           # Main HTML file
├── about.html           # Other pages
├── contact.html
├── css/
│   └── style.css        # Stylesheets
├── js/
│   └── main.js          # JavaScript files
├── images/
│   ├── logo.png
│   └── hero.jpg
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
└── .git/                # Git repository (hidden)
```

**Node.js/npm Project Structure**

For JavaScript projects using npm:

```
my-app/
├── package.json         # Project metadata and dependencies
├── package-lock.json    # Locked dependency versions
├── README.md
├── .gitignore
├── .env                 # Environment variables (not in git)
├── .env.example         # Example env variables
├── src/
│   ├── index.js         # Entry point
│   ├── components/      # Reusable components
│   └── utils/           # Helper functions
├── public/              # Static assets
│   ├── index.html
│   └── favicon.ico
├── tests/               # Test files
├── node_modules/        # Installed packages (not in git!)
└── dist/                # Built/compiled output
```

**React Project Structure**

When using Create React App or Vite:

```
my-react-app/
├── package.json
├── vite.config.js
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Footer.jsx
│   │   └── Button.jsx
│   ├── pages/
│   │   ├── Home.jsx
│   │   └── About.jsx
│   └── styles/
│       └── App.css
├── public/
│   └── index.html
└── dist/                # Built output
```

**Best Practices**

- **Consistency**: Use consistent naming conventions (kebab-case for folders, camelCase for JavaScript)
- **Grouping by Feature**: Group related files together
- **Separation of Concerns**: Keep components, styles, and logic separate
- **Don't Over-Organize**: Avoid too many nested folders; keep structure simple initially
- **Meaningful Names**: Folder and file names should be self-documenting
            """,
            
            "npm_projects": """
**What is package.json?**

The package.json file is the heart of a Node.js project. It contains:

```json
{
  "name": "my-awesome-app",
  "version": "1.0.0",
  "description": "A simple web application",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "build": "webpack"
  },
  "keywords": ["web", "app"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.0",
    "react": "^18.2.0"
  },
  "devDependencies": {
    "webpack": "^5.75.0",
    "jest": "^29.5.0"
  }
}
```

**Creating a package.json**

```bash
# Interactive initialization
npm init

# Quick initialization with defaults
npm init -y

# Or create manually with text editor
```

**Installing Dependencies**

```bash
# Install all dependencies from package.json
npm install

# Install a new package
npm install react

# Install as development dependency
npm install --save-dev webpack

# Install specific version
npm install react@18.2.0

# Remove a package
npm uninstall react
```

**Running Scripts**

Define scripts in package.json to automate tasks:

```bash
# npm run script-name
npm run dev        # Runs "dev" script
npm start          # Special script (no "run" needed)
npm test
```

**Understanding node_modules**

When you install packages, they go in `node_modules/`. This folder:
- Can be huge (hundreds of MB)
- Should NOT be committed to Git
- Should be listed in .gitignore
- Is recreated by running `npm install`

Always exclude it: add `node_modules/` to .gitignore.

**package-lock.json**

This file locks dependency versions. ALWAYS commit this to Git. It ensures:
- Everyone installs the same versions
- Reproducible builds
- Avoid version conflicts
            """,
            
            "initialization_steps": """
**For a Static HTML Project**

```bash
# Create project folder
mkdir my-website
cd my-website

# Initialize Git
git init

# Create folder structure
mkdir css js images

# Create main files
touch index.html
touch css/style.css
touch js/main.js

# Create .gitignore
echo "node_modules/\n.DS_Store\n.env" > .gitignore

# Create README
touch README.md

# Create basic HTML
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Website</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <h1>Welcome</h1>
  <script src="js/main.js"></script>
</body>
</html>
EOF

# Commit initial structure
git add .
git commit -m "Initial project structure"
```

**For a Node.js/npm Project**

```bash
# Create project folder
mkdir my-app
cd my-app

# Initialize npm
npm init -y

# Initialize Git
git init

# Create folder structure
mkdir src public tests

# Create basic files
touch src/index.js
touch public/index.html
touch README.md
touch .env.example

# Create .gitignore
cat > .gitignore << 'EOF'
node_modules/
.DS_Store
.env
dist/
*.log
EOF

# Create package.json scripts
# (Edit package.json to add scripts)

# Initial commit
git add .
git commit -m "Initial project setup"
```

**For a React Project (Using Vite)**

```bash
# Create React app with Vite
npm create vite@latest my-react-app -- --template react

# Navigate to project
cd my-react-app

# Install dependencies
npm install

# Initialize Git
git init

# Create .gitignore (Vite already creates this)
# View it: cat .gitignore

# Start development server
npm run dev

# Initial commit
git add .
git commit -m "Initial React setup"
```
            """,
            
            "essential_files": """
**README.md**

Every project needs a README explaining:
- What the project does
- How to install and run it
- How to contribute
- License information

Example:
```markdown
# My Awesome Website

A personal portfolio website built with HTML, CSS, and JavaScript.

## Getting Started

1. Clone the repository
2. Open index.html in your browser

## Features

- Responsive design
- Smooth animations
- Contact form

## License

MIT License
```

**.gitignore**

Lists files Git should ignore:

```
# OS files
.DS_Store
Thumbs.db

# Dependencies
node_modules/

# Environment variables
.env
.env.local

# Build output
dist/
build/

# Logs
*.log
npm-debug.log

# IDE
.vscode/
.idea/
*.swp
```

**.env Files**

Store sensitive data (API keys, database URLs) here:

```
# .env (don't commit this!)
API_KEY=secret123
DATABASE_URL=postgres://user:pass@localhost/db
```

Create `.env.example` showing what variables are needed:

```
# .env.example (commit this!)
API_KEY=
DATABASE_URL=
```

**.editorconfig**

Ensures consistent code style across editors:

```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true

[*.{js,jsx,ts,tsx}]
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

**.prettierrc**

Configure Prettier code formatter:

```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

**.eslintrc.json**

Configure ESLint for code quality:

```json
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": "eslint:recommended",
  "rules": {
    "no-unused-vars": "warn"
  }
}
```
            """
        }
    },
    
    "key_takeaways": [
        "Proper project structure makes work easier and more scalable",
        "package.json is the core of npm projects",
        "Always initialize Git right from the start",
        ".gitignore prevents tracking unnecessary files",
        "Environment variables keep secrets out of version control",
        "README documentation is essential",
        "Different project types have different structures",
        "Taking time to set up properly saves time later"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Initialize a static HTML project with proper structure",
            "Create an npm project and add some dependencies",
            "Write a comprehensive README.md",
            "Create a .gitignore and understand what to exclude",
            "Set up .env and .env.example files",
            "Initialize a React project and explore its structure",
            "Configure ESLint and Prettier for code quality",
            "Practice the complete initialization workflow from scratch"
        ],
        "discussion_questions": [
            "Why is folder structure important as projects grow?",
            "What should always go in .gitignore?",
            "What's the difference between dependencies and devDependencies?",
            "Why create both .env and .env.example?",
            "How does proper initialization affect team collaboration?",
            "What's the purpose of package-lock.json?"
        ]
    },
    
    "related_topics": [
        "Git and Version Control",
        "Command Line Basics",
        "Node.js and npm",
        "Development Environment Setup"
    ]
}
