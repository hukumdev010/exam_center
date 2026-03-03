"""
Code Editors and IDEs - Detailed Content

This file contains content for the "Code Editors and IDEs" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Code Editors and IDEs",
    "duration": "10-15 minutes",
    "difficulty": "Beginner",
    "overview": """
    A good code editor is essential for productive development. This topic covers the differences between simple
    text editors and full IDEs, popular choices for web development, and how to set up your development environment.
    """,
    
    "detailed_content": {
        "introduction": """
You're about to spend thousands of hours writing code. The tool you use to write that code—your editor—has an enormous
impact on your productivity, happiness, and the quality of your work.

The good news: you have excellent choices available, and many are free or very affordable. The key is finding an editor
that matches your workflow and learning curve.

There's a spectrum from simple text editors to full-featured IDEs (Integrated Development Environments), each with
different tradeoffs in features, speed, and learning curve.
        """,
        
        "key_concepts": {
            "text_editors_vs_ides": """
**Text Editors**

Simple programs designed to edit text files. Lightweight and fast.

**Pros**:
- Fast to start up
- Minimal learning curve
- Customizable
- Great for small projects

**Cons**:
- Fewer built-in features
- Need to install extensions for many features
- Less integrated workflow

**Popular Text Editors**:
- VS Code
- Sublime Text
- Atom
- Vim / Neovim

**IDEs (Integrated Development Environments)**

Comprehensive development platforms with built-in tools.

**Pros**:
- Powerful built-in features
- Integrated debugging, testing, and version control
- Project-aware (understands your entire project structure)
- Excellent refactoring tools
- More intelligent code completion

**Cons**:
- Heavier and slower
- Steeper learning curve
- Can feel overwhelming for beginners
- Often expensive

**Popular IDEs**:
- JetBrains WebStorm (paid, but excellent for web development)
- JetBrains IntelliJ IDEA (paid, works for many languages)
- Visual Studio (Microsoft, mostly for .NET)
- NetBeans (free, Java-focused)

**For Web Development**: VS Code has become the industry standard. It offers a great balance of lightweight speed
with IDE-like features through extensions.
            """,
            
            "vs_code": """
**Why VS Code Dominates Web Development**

VS Code is used by the vast majority of web developers because:

- **Built by Microsoft**: Regular updates and professional support
- **Free and Open Source**: No licensing costs
- **Lightweight**: Starts fast, runs smoothly
- **Extensive Extensions**: Thousands of plugins for every tool and language
- **Great for Web Dev**: Built-in support for JavaScript, HTML, CSS
- **Integrated Terminal**: Run commands without leaving the editor
- **Excellent Git Integration**: Built-in Git support
- **IntelliSense**: Smart code completion based on your code structure

**Essential VS Code Features**:

**Command Palette** (Ctrl+Shift+P):
Access any VS Code command by name. This is incredibly powerful. Try:
- "Format Document" to auto-format code
- "Go to File" to jump to any file in your project
- "Extensions" to install plugins

**Multi-Cursor Editing** (Ctrl+Alt+Click):
Click multiple places to edit multiple lines simultaneously. Saves tons of time.

**Find and Replace** (Ctrl+H):
Search the entire project and replace text. Supports regular expressions.

**Integrated Git** (Ctrl+Shift+G):
Stage commits, view diffs, manage branches without leaving the editor.

**Integrated Terminal** (Ctrl+`):
Run commands right in the editor. Perfect for running npm scripts, git commands, etc.

**Extensions**:
Must-have extensions for web development:
- **ESLint**: Lints JavaScript code, catches errors and style issues
- **Prettier**: Auto-formats code, saves style discussions
- **Thunder Client or REST Client**: Test APIs without leaving the editor
- **Git Graph**: Visualize your git history
- **Live Server**: Preview HTML files with auto-refresh
- **React, Vue, Svelte Extensions**: Language-specific support
- **Docker, Kubernetes**: If doing DevOps work

**Settings and Themes**:
Customize VS Code to your preferences:
- Choose from many themes (Dark, Light, High Contrast)
- Configure font, size, and formatting
- Customize keyboard shortcuts
- Configure extensions
            """,
            
            "setting_up_development": """
**Your Development Environment**

Beyond the editor, you need a complete development environment:

**Terminal/Command Line**:
A terminal is essential for:
- Running build commands
- Using version control (git)
- Running servers and tests
- Installing packages

On Windows: CMD, PowerShell, or WSL (Windows Subsystem for Linux)
On Mac/Linux: Terminal (or iTerm2, Zsh, Fish)

**Node.js and npm**:
For JavaScript development, install Node.js (which includes npm):
- Node.js is a JavaScript runtime for servers
- npm is the package manager for JavaScript

Check if installed:
```bash
node --version
npm --version
```

**Git**:
Version control is essential. Most projects use Git.

Check if installed:
```bash
git --version
```

**Package Manager**:
JavaScript projects use package managers:
- **npm**: Most common, comes with Node.js
- **yarn**: Alternative, slightly better for monorepos
- **pnpm**: Newer, faster alternative

**Development Directory Structure**:

Create a folder for your projects:
```
~/Developer/
├── project1/
├── project2/
└── learning/
```

Keep projects organized, one folder per project.

**Working with Projects**:

To work on a project in VS Code:
1. Open VS Code
2. File > Open Folder
3. Select your project folder
4. VS Code loads the project
5. Open Terminal (Ctrl+`)
6. Start coding!

**Project Package.json**:

Every JavaScript project has a package.json file that lists:
- Project metadata (name, version, description)
- Dependencies (packages your project needs)
- Scripts (commands to run like npm start)

Example:
```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  }
}
```
            """,
            
            "best_practices": """
**Keyboard Shortcuts**

Learn keyboard shortcuts for your editor. This dramatically speeds up coding:

**VS Code Essentials**:
- Ctrl+P: Open file by name
- Ctrl+Shift+P: Command palette
- Ctrl+F: Find
- Ctrl+H: Find and replace
- Ctrl+K Ctrl+0: Fold all
- Ctrl+K Ctrl+J: Unfold all
- Ctrl+Alt+Down: Copy line down
- Ctrl+Shift+K: Delete line
- Alt+Up/Down: Move line up/down

**Workspace Management**

- Keep your project organized
- Use consistent folder structure
- Don't mix multiple projects in one folder
- Use .gitignore to exclude files from version control
- Keep node_modules out of version control (add to .gitignore)

**Extensions Wisdom**

- Don't install too many extensions (slows down the editor)
- Install only what you actually use
- Review extension updates
- Keep your editor lean and fast
            """
        }
    },
    
    "key_takeaways": [
        "VS Code is the industry standard for web development",
        "A good editor dramatically impacts your productivity",
        "Set up your development environment properly from the start",
        "Learn keyboard shortcuts to work faster",
        "Node.js and npm are essential for JavaScript development",
        "Git and a terminal are crucial tools",
        "Keep your projects organized and structured",
        "Invest time in learning your editor well"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Download and install VS Code if you haven't already",
            "Install essential extensions: ESLint, Prettier, Thunder Client",
            "Customize your editor theme and settings",
            "Learn the top 10 keyboard shortcuts for your editor",
            "Install Node.js and npm, verify they work",
            "Create a test project folder and open it in VS Code",
            "Create a package.json file manually",
            "Open the integrated terminal and run a command",
            "Try multi-cursor editing with Ctrl+Alt+Click"
        ],
        "discussion_questions": [
            "Why has VS Code become the dominant editor for web development?",
            "What's the difference between a text editor and an IDE?",
            "Why is a terminal important for development?",
            "How do extensions enhance your development workflow?",
            "What's the role of Node.js and npm in web development?"
        ]
    },
    
    "related_topics": [
        "Command Line Basics",
        "Git and Version Control",
        "Project Initialization",
        "Developer Tools and DevTools"
    ]
}
