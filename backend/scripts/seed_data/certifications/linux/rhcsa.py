"""Red Hat Certified System Administrator (RHCSA) Certification"""

CERTIFICATION = {
    "name": "Red Hat Certified System Administrator (RHCSA)",
    "description": "Red Hat Enterprise Linux system administration skills",
    "slug": "rhcsa",
    "level": "Professional",
    "duration": 150,
    "questions_count": 15,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which command is used to manage systemd services in RHEL?",
        "explanation": "The systemctl command is the primary tool for managing systemd services in Red Hat Enterprise Linux and other systemd-based distributions.",
        "reference": "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-services-with-systemd_configuring-basic-system-settings",
        "points": 1,
        "answers": [
            {"text": "service", "is_correct": False},
            {"text": "systemctl", "is_correct": True},
            {"text": "chkconfig", "is_correct": False},
            {"text": "init", "is_correct": False}
        ]
    }
]
