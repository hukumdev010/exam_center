"""SUSE Certified Linux Administrator (CLA)"""

CERTIFICATION = {
    "name": "SUSE Certified Linux Administrator (CLA)",
    "description": "SUSE Linux Enterprise administration and management skills",
    "slug": "suse-cla",
    "level": "Professional",
    "duration": 90,
    "questions_count": 45,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which package manager is primarily used in SUSE Linux Enterprise?",
        "explanation": "SUSE Linux Enterprise uses zypper as its primary package manager for installing, updating, and removing software packages.",
        "reference": "https://documentation.suse.com/sles/15-SP3/html/SLES-all/cha-sw-cl.html",
        "points": 1,
        "answers": [
            {"text": "yum", "is_correct": False},
            {"text": "apt", "is_correct": False},
            {"text": "zypper", "is_correct": True},
            {"text": "dnf", "is_correct": False}
        ]
    },
    {
        "text": "What is YaST in SUSE Linux?",
        "explanation": "YaST (Yet another Setup Tool) is SUSE's comprehensive system administration and configuration tool with both GUI and text-based interfaces.",
        "reference": "https://documentation.suse.com/sles/15-SP3/html/SLES-all/cha-yast-text.html",
        "points": 1,
        "answers": [
            {"text": "A text editor", "is_correct": False},
            {"text": "System administration tool", "is_correct": True},
            {"text": "Package repository", "is_correct": False},
            {"text": "File manager", "is_correct": False}
        ]
    },
    {
        "text": "Which command is used to list all available repositories in SUSE?",
        "explanation": "The 'zypper lr' or 'zypper repos' command lists all configured software repositories in SUSE Linux systems.",
        "reference": "https://documentation.suse.com/sles/15-SP3/html/SLES-all/sec-zypper-softman.html",
        "points": 1,
        "answers": [
            {"text": "zypper list", "is_correct": False},
            {"text": "zypper lr", "is_correct": True},
            {"text": "zypper show", "is_correct": False},
            {"text": "zypper search", "is_correct": False}
        ]
    },
    {
        "text": "What is the default init system in modern SUSE Linux Enterprise?",
        "explanation": "Modern SUSE Linux Enterprise Server uses systemd as its init system for managing services and system processes.",
        "reference": "https://documentation.suse.com/sles/15-SP3/html/SLES-all/cha-systemd.html",
        "points": 1,
        "answers": [
            {"text": "SysV init", "is_correct": False},
            {"text": "systemd", "is_correct": True},
            {"text": "Upstart", "is_correct": False},
            {"text": "OpenRC", "is_correct": False}
        ]
    },
    {
        "text": "Which tool is used for network configuration in SUSE Linux?",
        "explanation": "Wicked is SUSE's network configuration framework that replaced the traditional ifup/ifdown scripts for network interface management.",
        "reference": "https://documentation.suse.com/sles/15-SP3/html/SLES-all/cha-network.html",
        "points": 1,
        "answers": [
            {"text": "NetworkManager", "is_correct": False},
            {"text": "Wicked", "is_correct": True},
            {"text": "netplan", "is_correct": False},
            {"text": "ifupdown", "is_correct": False}
        ]
    }
]
