"""Linux Professional Institute Certification Level 2 (LPIC-2)"""

CERTIFICATION = {
    "name": "Linux Professional Institute Certification Level 2 (LPIC-2)",
    "description": "Advanced Linux professional skills and knowledge",
    "slug": "lpic-2",
    "level": "Professional",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which command is used to configure kernel modules to load automatically at boot time?",
        "explanation": "The /etc/modules-load.d/ directory contains configuration files that specify kernel modules to load at boot time. Files should have .conf extension.",
        "reference": "https://www.lpi.org/our-certifications/lpic-2-overview",
        "points": 1,
        "answers": [
            {"text": "modprobe", "is_correct": False},
            {"text": "insmod", "is_correct": False},
            {"text": "/etc/modules-load.d/*.conf", "is_correct": True},
            {"text": "/etc/modprobe.conf", "is_correct": False}
        ]
    },
    {
        "text": "What is the default log level for the Linux kernel?",
        "explanation": "The default kernel log level is 4 (KERN_WARNING), which means messages with priority 4 and lower (higher priority) are displayed on the console.",
        "reference": "https://www.kernel.org/doc/html/latest/core-api/printk-basics.html",
        "points": 1,
        "answers": [
            {"text": "0", "is_correct": False},
            {"text": "4", "is_correct": True},
            {"text": "7", "is_correct": False},
            {"text": "1", "is_correct": False}
        ]
    },
    {
        "text": "Which file contains the system's current kernel parameters?",
        "explanation": "/proc/cmdline contains the kernel command line parameters that were passed to the kernel at boot time.",
        "reference": "https://www.kernel.org/doc/Documentation/filesystems/proc.txt",
        "points": 1,
        "answers": [
            {"text": "/proc/version", "is_correct": False},
            {"text": "/proc/cmdline", "is_correct": True},
            {"text": "/proc/cpuinfo", "is_correct": False},
            {"text": "/proc/meminfo", "is_correct": False}
        ]
    },
    {
        "text": "What command is used to display and configure network interface parameters?",
        "explanation": "The ip command is the modern replacement for ifconfig and is used to display and configure network interfaces, routing, and tunnels.",
        "reference": "https://man7.org/linux/man-pages/man8/ip.8.html",
        "points": 1,
        "answers": [
            {"text": "ifconfig", "is_correct": False},
            {"text": "ip", "is_correct": True},
            {"text": "netstat", "is_correct": False},
            {"text": "route", "is_correct": False}
        ]
    },
    {
        "text": "Which directory contains systemd unit files for system services?",
        "explanation": "/lib/systemd/system/ contains the default systemd unit files installed by packages, while /etc/systemd/system/ contains local customizations.",
        "reference": "https://www.freedesktop.org/software/systemd/man/systemd.unit.html",
        "points": 1,
        "answers": [
            {"text": "/etc/systemd/", "is_correct": False},
            {"text": "/lib/systemd/system/", "is_correct": True},
            {"text": "/usr/systemd/", "is_correct": False},
            {"text": "/var/systemd/", "is_correct": False}
        ]
    }
]
