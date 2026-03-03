"""
Git and Version Control - Detailed Content

This file contains content for the "Git and Version Control" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Git and Version Control",
    "duration": "10-15 minutes",
    "difficulty": "Beginner",
    "overview": """
    Git is a version control system that tracks changes to your code over time. It's essential for every developer,
    enabling collaboration, maintaining history, and safely experimenting with new features. This topic covers Git
    fundamentals, common workflows, and how to use GitHub.
    """,
    
    "detailed_content": {
        "introduction": """
Imagine working on a document, and after every major change, you saved a snapshot of that document. Later, if you
made a mistake, you could go back to any previous snapshot. You could also have multiple versions of the document
being worked on simultaneously, and then merge them back together.

That's what version control does for code. Git is by far the most popular version control system. It's used by
virtually every professional development team and open-source project.

Without version control, you'd have files like:
- project-final.js
- project-final-v2.js
- project-final-actual.js
- project-final-REALLY-FINAL.js

With Git, you have one file and a complete history of every change ever made to it.
        """,
        
        "key_concepts": {
            "why_version_control": """
**Problem It Solves**

Without version control:
- No history of changes—can't see what changed or when
- No way to undo mistakes—if you delete something, it's gone
- No collaboration—hard for teams to work on the same code
- No branches—can't safely experiment with new features
- No backup—code exists only on your computer

**What Git Provides**

- **History**: Every change is recorded with timestamp and author
- **Branches**: Work on features independently without affecting main code
- **Merging**: Combine work from multiple people safely
- **Reverting**: Undo mistakes by going back to any previous version
- **Collaboration**: Multiple developers can work on the same project
- **Backup**: Code stored on remote servers (like GitHub)
- **Tracking**: See exactly what changed and why

**Real-World Example**

Your team is building a website. One developer works on a login feature, another on the home page, another on the
database. With Git, they can:
1. Each work on their own branch without interfering
2. Save their work regularly with commits
3. Review each other's code before merging
4. Safely combine everyone's work
5. If something breaks, revert to the last working version

This would be impossible without version control.
            """,
            
            "git_basics": """
**Key Concepts**

**Repository (Repo)**: A project folder tracked by Git. Contains all your code and Git history.

**Commit**: A snapshot of your code at a point in time. Each commit has:
- A unique ID (hash)
- Author information
- Timestamp
- A message describing what changed
- The actual code changes

**Branch**: An independent line of development. Usually you have:
- `main`: The official, production-ready code
- `develop`: Development version
- `feature/login`: Feature branches for specific features

**Remote**: A copy of your repository on a server like GitHub, GitLab, or Bitbucket. Usually called `origin`.

**Working Directory**: Your local files on your computer that you're actively editing.

**Staging Area**: Files you've marked to be included in the next commit.

**The Three States**

1. **Modified**: You've changed files but haven't saved them to Git
2. **Staged**: You've marked changes to be committed
3. **Committed**: Changes are saved in Git history
            """,
            
            "essential_commands": """
**Setup**

```bash
# Configure your name and email (one time)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Check configuration
git config --list
```

**Creating and Cloning**

```bash
# Create a new repository
git init

# Clone an existing repository
git clone https://github.com/user/repo.git
cd repo
```

**Checking Status**

```bash
# See current status
git status

# See what you've changed
git diff

# See staged changes
git diff --staged
```

**Making Changes**

```bash
# Stage specific file
git add filename.js

# Stage all changes
git add .

# Unstage a file
git reset filename.js

# Discard changes (careful—can't undo)
git restore filename.js
```

**Committing**

```bash
# Commit staged changes with a message
git commit -m "Fix login bug"

# See commit history
git log
git log --oneline      # Shorter format
git log -p             # Shows actual changes

# Show a specific commit
git show commit-id
```

**Branches**

```bash
# Create and switch to new branch
git checkout -b feature/login

# Or (newer syntax)
git switch -c feature/login

# List branches
git branch
git branch -a          # All branches including remote

# Switch branch
git checkout develop
git switch develop     # Newer syntax

# Delete branch
git branch -d feature/login
git branch -D feature/login  # Force delete

# Rename branch
git branch -m new-name
```

**Merging**

```bash
# Switch to branch you want to merge into
git switch main

# Merge another branch
git merge feature/login

# If conflicts occur, resolve them, then:
git add .
git commit -m "Merge feature/login"
```

**Remote Operations**

```bash
# See remote repositories
git remote -v

# Push changes to remote
git push origin main
git push origin feature/login

# Pull changes from remote
git pull origin main

# Fetch without merging
git fetch origin

# Set upstream branch
git push -u origin feature/login
```

**Undoing Changes**

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert a commit (creates new commit undoing it)
git revert commit-id

# Go back in time (detached state)
git checkout commit-id
```
            """,
            
            "workflow_example": """
**Typical Development Workflow**

```bash
# 1. Start with latest code
git pull origin develop

# 2. Create feature branch
git checkout -b feature/user-profile

# 3. Make changes
# (edit files)

# 4. Check what changed
git status
git diff

# 5. Stage and commit
git add .
git commit -m "Add user profile page"

# 6. Push to remote
git push origin feature/user-profile

# 7. Create Pull Request on GitHub (web interface)
# Teammates review your code

# 8. Once approved, merge into develop
# (can do via GitHub web interface)

# 9. Update local develop
git checkout develop
git pull origin develop

# 10. Delete feature branch
git branch -d feature/user-profile
git push origin --delete feature/user-profile
```

**When Something Goes Wrong**

```bash
# Accidentally committed to wrong branch?
git reset --soft HEAD~1  # Undo commit, keep changes
git checkout correct-branch
git commit -m "message"

# Merged the wrong branch?
git revert commit-id     # Create new commit undoing it

# Lost your changes?
git reflog               # See all actions
git checkout commit-id   # Recover

# Messy commits before pushing?
git rebase -i HEAD~3     # Interactively rewrite last 3 commits
```
            """,
            
            "github_and_collaboration": """
**GitHub Basics**

GitHub is a cloud platform for hosting Git repositories. It's where the world's open-source code lives.

**Setting Up GitHub**

1. Create account at github.com
2. Create new repository
3. Clone it locally: `git clone URL`
4. Make changes and commit
5. Push to GitHub: `git push origin main`
6. See your code at github.com

**Pull Requests**

A Pull Request (PR) is a way to propose changes:
1. Create a feature branch
2. Make commits
3. Push branch to GitHub
4. Click "Create Pull Request"
5. Write description of changes
6. Teammates review code
7. Discuss and request changes if needed
8. Once approved, merge

Pull requests are crucial for code review and team collaboration.

**Issues and Discussions**

GitHub also provides:
- **Issues**: Track bugs and feature requests
- **Discussions**: Ask questions and share ideas
- **Projects**: Kanban-style project management
- **Wiki**: Documentation

**Collaboration Best Practices**

- Write clear commit messages
- Create small, focused commits
- Use descriptive branch names
- Write good pull request descriptions
- Review teammates' code thoughtfully
- Keep branches up-to-date with main
- Delete merged branches
            """
        }
    },
    
    "key_takeaways": [
        "Git is essential version control for all developers",
        "Commits are snapshots of your code at points in time",
        "Branches allow independent work on features",
        "Pull requests enable code review and collaboration",
        "Always write clear commit messages",
        "GitHub is the most popular platform for hosting code",
        "Master Git basics now—you'll use it daily",
        "Version control is not optional; it's mandatory in professional development"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Initialize a Git repository in a test folder",
            "Create some files, make commits with different messages",
            "Create multiple branches and switch between them",
            "Make changes on different branches and merge them",
            "Create a GitHub account and push a repository",
            "Practice viewing commit history and understanding what changed",
            "Try undoing a commit and understanding the difference between reset and revert",
            "Simulate a merge conflict and practice resolving it"
        ],
        "discussion_questions": [
            "Why is version control essential in team development?",
            "What's the difference between a commit and a branch?",
            "How do pull requests improve code quality?",
            "What information should a good commit message contain?",
            "Why might you want to keep related changes separate?",
            "How do merge conflicts occur and how do you resolve them?"
        ]
    },
    
    "related_topics": [
        "Command Line Basics",
        "GitHub and Collaboration",
        "Project Initialization",
        "Development Workflow"
    ]
}
