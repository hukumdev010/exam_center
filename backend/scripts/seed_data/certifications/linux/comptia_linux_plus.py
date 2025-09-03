"""CompTIA Linux+ Certification"""

CERTIFICATION = {
    "name": "CompTIA Linux+",
    "description": "Linux system administration and troubleshooting skills",
    "slug": "comptia-linux-plus",
    "level": "Professional",
    "duration": 90,
    "questions_count": 90,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which command is used to change file permissions in Linux?",
        "explanation": "The chmod command is used to change file and directory permissions in Linux systems.",
        "reference": "https://man7.org/linux/man-pages/man1/chmod.1.html",
        "points": 1,
        "answers": [
            {"text": "chown", "is_correct": False},
            {"text": "chmod", "is_correct": True},
            {"text": "chgrp", "is_correct": False},
            {"text": "umask", "is_correct": False}
        ]
    },
    {
        "text": "What does the 'ps aux' command display?",
        "explanation": "The 'ps aux' command shows detailed information about all running processes including user, CPU usage, memory usage, and command.",
        "reference": "https://man7.org/linux/man-pages/man1/ps.1.html",
        "points": 1,
        "answers": [
            {"text": "Network connections", "is_correct": False},
            {"text": "File system usage", "is_correct": False},
            {"text": "Running processes", "is_correct": True},
            {"text": "System logs", "is_correct": False}
        ]
    }
]
