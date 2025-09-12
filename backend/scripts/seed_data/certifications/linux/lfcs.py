"""Linux Foundation Certified System Administrator (LFCS)"""

CERTIFICATION = {
    "name": "Linux Foundation Certified System Administrator (LFCS)",
    "description": "Performance-based Linux system administration certification",
    "slug": "lfcs",
    "level": "Professional",
    "duration": 120,
    "questions_count": 24,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which command is used to create a logical volume in LVM?",
        "explanation": "The lvcreate command is used to create logical volumes within a volume group in Linux Logical Volume Management (LVM).",
        "reference": "https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/",
        "points": 1,
        "answers": [
            {"text": "lvextend", "is_correct": False},
            {"text": "lvcreate", "is_correct": True},
            {"text": "vgcreate", "is_correct": False},
            {"text": "pvcreate", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary purpose of the /etc/fstab file?",
        "explanation": "/etc/fstab contains information about filesystems and their mount points, used for automatic mounting at boot time.",
        "reference": "https://man7.org/linux/man-pages/man5/fstab.5.html",
        "points": 1,
        "answers": [
            {"text": "Store user passwords", "is_correct": False},
            {"text": "Configure filesystem mounts", "is_correct": True},
            {"text": "Define network interfaces", "is_correct": False},
            {"text": "Manage system services", "is_correct": False}
        ]
    },
    {
        "text": "Which command displays real-time process information?",
        "explanation": "The top command displays real-time information about running processes, including CPU and memory usage.",
        "reference": "https://man7.org/linux/man-pages/man1/top.1.html",
        "points": 1,
        "answers": [
            {"text": "ps", "is_correct": False},
            {"text": "top", "is_correct": True},
            {"text": "pstree", "is_correct": False},
            {"text": "jobs", "is_correct": False}
        ]
    },
    {
        "text": "What command is used to change file permissions using symbolic notation?",
        "explanation": "The chmod command can use symbolic notation (like chmod u+x file) to change file permissions for user, group, and others.",
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
        "text": "Which systemctl command enables a service to start automatically at boot?",
        "explanation": "The 'systemctl enable' command creates symbolic links to enable a service to start automatically during the boot process.",
        "reference": "https://www.freedesktop.org/software/systemd/man/systemctl.html",
        "points": 1,
        "answers": [
            {"text": "systemctl start", "is_correct": False},
            {"text": "systemctl enable", "is_correct": True},
            {"text": "systemctl activate", "is_correct": False},
            {"text": "systemctl boot", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of the crontab command?",
        "explanation": "The crontab command is used to view, edit, and manage user cron jobs for scheduling tasks to run automatically.",
        "reference": "https://man7.org/linux/man-pages/man1/crontab.1.html",
        "points": 1,
        "answers": [
            {"text": "Manage system processes", "is_correct": False},
            {"text": "Schedule automated tasks", "is_correct": True},
            {"text": "Monitor system logs", "is_correct": False},
            {"text": "Configure network settings", "is_correct": False}
        ]
    }
]
