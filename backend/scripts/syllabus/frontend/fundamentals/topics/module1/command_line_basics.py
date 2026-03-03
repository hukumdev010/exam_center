"""
Command Line Basics - Detailed Content

This file contains content for the "Command Line Basics" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Command Line Basics",
    "duration": "10-15 minutes",
    "difficulty": "Beginner",
    "overview": """
    The command line is a text-based interface to your computer. For web developers, the command line is
    essential for running build tools, managing version control, and automating tasks. This topic covers
    fundamental command line concepts and the most common commands you'll use daily.
    """,
    
    "detailed_content": {
        "introduction": """
If you grew up with graphical interfaces (windows, buttons, icons), the command line might seem intimidating at first.
But it's actually incredibly powerful and, once you learn the basics, much faster than clicking through menus.

The command line (also called terminal, shell, or console) is where you type text commands to tell your computer what
to do. Web developers spend a significant portion of their time in the command line:

- Running development servers
- Installing packages and dependencies
- Managing version control with Git
- Running tests and build tools
- Deploying applications
- Automating repetitive tasks

Mastering the command line is one of the most important skills you can develop as a developer.
        """,
        
        "key_concepts": {
            "opening_terminal": """
**Windows**:
- Click Start menu, search for "Command Prompt" or "PowerShell"
- Or use Windows Terminal (recommended)
- For better experience, use WSL (Windows Subsystem for Linux)

**Mac**:
- Applications > Utilities > Terminal
- Or use iTerm2 (popular third-party alternative)
- Or use Zsh (default on newer macOS)

**Linux**:
- Usually Ctrl+Alt+T or available in application menu

**In VS Code**:
- Press Ctrl+` (backtick) to open integrated terminal
- This is the most convenient way to use terminal while coding

**What You'll See**:
```
username@computer ~ $
```

This prompt is ready for you to type commands. The `~` means you're in your home directory.
            """,
            
            "core_concepts": """
**Paths and Directories**

Everything on your computer is organized in folders (directories) in a tree structure:

```
/
├── Users (or home on Linux)
│   └── yourname
│       ├── Desktop
│       ├── Documents
│       └── Developer
├── Applications
└── var
```

Paths describe where something is:
- `/Users/yourname/Developer` - Absolute path (starts with /)
- `Desktop` - Relative path (relative to current location)
- `..` - Parent directory
- `~` - Home directory
- `.` - Current directory

**Current Working Directory**

You're always "in" a directory. The prompt shows where you are. You can navigate around using commands.

**File Permissions**

Files have read (r), write (w), and execute (x) permissions for owner, group, and others. This controls who can
access and modify files.

**Root vs Regular User**

- **Root**: Administrator with access to everything (use carefully!)
- **Regular User**: Limited access for safety

**Pipes and Redirection**

- `>` redirects output to a file: `echo "hello" > file.txt`
- `|` pipes output from one command to another: `cat file.txt | grep "hello"`
- `>>` appends to a file instead of overwriting
            """,
            
            "essential_commands": """
**Navigation Commands**

```bash
# Print working directory - shows where you are
pwd

# List files in current directory
ls
ls -la          # Detailed list with hidden files
ls -l           # Long format with permissions

# Change directory
cd Desktop      # Go to Desktop folder
cd ..           # Go up one level
cd ~            # Go to home directory
cd /            # Go to root
```

**File Management**

```bash
# Create a new file (empty)
touch filename.txt

# Create a new directory
mkdir folder-name
mkdir -p folder/subfolder    # Create parent folders too

# Copy files
cp source.txt destination.txt
cp -r folder1 folder2        # Copy entire folder

# Move or rename
mv old-name.txt new-name.txt
mv file.txt folder/          # Move file to folder

# Delete files (careful—no undo!)
rm file.txt
rm -r folder/                # Delete folder and contents

# Show file contents
cat file.txt
less file.txt                # View with pagination

# Edit files
nano file.txt                # Simple text editor
vim file.txt                 # Advanced editor (steeper learning curve)
```

**Directory Operations**

```bash
# Show current directory contents
ls

# Show directory tree structure
tree
# or
ls -R

# Show disk usage
du -sh *           # Size of each file/folder in current directory

# Find files
find . -name "*.js"    # Find all JavaScript files
find . -name "file*"   # Files starting with "file"
```

**Text Operations**

```bash
# Search within files
grep "search-term" file.txt
grep -r "term" .        # Search all files in current directory

# Count lines
wc -l file.txt

# Print first/last lines
head -n 5 file.txt      # First 5 lines
tail -n 5 file.txt      # Last 5 lines

# Sort
sort file.txt

# Combine and display
cat file1.txt file2.txt
```

**Permissions**

```bash
# Change permissions
chmod 755 script.sh         # Make file executable
chmod -r x folder/          # Remove execute permission recursively

# Change owner
chown user:group file.txt
```
            """,
            
            "practical_workflows": """
**Setting Up a Project**

```bash
# Navigate to projects directory
cd ~/Developer

# Create new project folder
mkdir my-project
cd my-project

# Initialize as Node.js project (creates package.json)
npm init -y

# Create src folder
mkdir src

# Create main files
touch src/index.js
touch package.json
touch README.md

# See what we created
ls -la
```

**Running Node.js and npm**

```bash
# Install a package
npm install react

# Install dev dependency (only for development)
npm install --save-dev eslint

# Run a script from package.json
npm start
npm run dev
npm test

# Install all dependencies listed in package.json
npm install
```

**Using Git**

```bash
# Initialize a new repository
git init

# Check status
git status

# Stage changes
git add .

# Commit changes
git commit -m "Initial commit"

# See history
git log

# Push to remote
git push origin main
```

**Useful Patterns**

```bash
# Clear the screen
clear

# See command history
history

# Repeat last command
!!

# Run command with elevated privileges
sudo command-name

# Run command in background
command-name &

# Kill a running process
kill process-id

# Show current user
whoami

# Show current date/time
date
```
            """,
            
            "tips_and_tricks": """
**Tab Completion**

Type part of a command or filename and press Tab. The terminal autocompletes it. This saves time and prevents typos.

```bash
cd De[TAB]  # Becomes cd Desktop/
ls file[TAB]  # Becomes ls file.txt
```

**Command History**

Press Up arrow to cycle through previously used commands. Faster than retyping.

```bash
npm start       # Run this
[UP arrow]      # Brings back "npm start"
```

**Man Pages**

Get help on any command:

```bash
man ls          # Shows manual for ls command
man grep        # Shows manual for grep command
```

**Aliases**

Create shortcuts for common commands in your shell configuration:

```bash
alias ll='ls -la'
alias gs='git status'
alias dev='cd ~/Developer'
```

**Hidden Files**

Files starting with `.` are hidden. Show them with `ls -a` or `ls -la`.

```bash
.gitignore      # Hidden git configuration
.env            # Hidden environment variables
.DS_Store       # macOS hidden file (usually want to ignore)
```

**Wildcards**

Use `*` to match multiple files:

```bash
rm *.log        # Delete all log files
cp *.js src/    # Copy all JavaScript files to src
ls *.{js,ts}    # List JavaScript and TypeScript files
```

**Output to File**

```bash
ls > files.txt      # Save output to file
echo "note" >> notes.txt  # Append to file
command > output.log 2>&1  # Save output and errors
```
            """
        }
    },
    
    "key_takeaways": [
        "The command line is essential for modern web development",
        "Understand paths, permissions, and directory structure",
        "Learn core navigation and file management commands",
        "Use tab completion and arrow keys for efficiency",
        "npm and git are the most important tools for web developers",
        "The command line is faster for many tasks than graphical interfaces",
        "Invest time learning command line basics—it pays dividends"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Open your terminal and navigate to different folders",
            "Create a test directory structure with mkdir",
            "Create and edit files using touch and nano/vim",
            "Practice tab completion by typing partial commands",
            "Use ls with different flags and see the differences",
            "Search for files using find and grep",
            "Install a package using npm and see what files it creates",
            "View and understand your PATH variable"
        ],
        "discussion_questions": [
            "Why do developers spend time in the command line instead of using graphical interfaces?",
            "What are the advantages of understanding paths and permissions?",
            "How does tab completion save time in development?",
            "Why is the command line important for version control?"
        ]
    },
    
    "related_topics": [
        "Git and Version Control",
        "Code Editors and IDEs",
        "Project Initialization",
        "Node.js and npm"
    ]
}
