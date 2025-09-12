"""Ubuntu Server Professional Certification"""

CERTIFICATION = {
    "name": "Ubuntu Server Professional Certification",
    "description": "Ubuntu Server administration and management expertise",
    "slug": "ubuntu-server-pro",
    "level": "Professional",
    "duration": 90,
    "questions_count": 50,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which package manager is used in Ubuntu Server?",
        "explanation": "Ubuntu Server uses apt (Advanced Package Tool) as its primary package manager for installing, updating, and removing software packages.",
        "reference": "https://ubuntu.com/server/docs/package-management",
        "points": 1,
        "answers": [
            {"text": "yum", "is_correct": False},
            {"text": "apt", "is_correct": True},
            {"text": "zypper", "is_correct": False},
            {"text": "pacman", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of cloud-init in Ubuntu Server?",
        "explanation": "Cloud-init is used for initial configuration of cloud instances, handling user data, SSH keys, package installation, and other setup tasks during first boot.",
        "reference": "https://cloudinit.readthedocs.io/en/latest/",
        "points": 1,
        "answers": [
            {"text": "Package management", "is_correct": False},
            {"text": "Cloud instance initialization", "is_correct": True},
            {"text": "Network monitoring", "is_correct": False},
            {"text": "Container orchestration", "is_correct": False}
        ]
    },
    {
        "text": "Which command is used to configure network interfaces in Ubuntu Server 20.04+?",
        "explanation": "Ubuntu Server 20.04+ uses netplan for network configuration, which generates configuration for NetworkManager or systemd-networkd.",
        "reference": "https://netplan.io/",
        "points": 1,
        "answers": [
            {"text": "ifconfig", "is_correct": False},
            {"text": "netplan", "is_correct": True},
            {"text": "nmcli", "is_correct": False},
            {"text": "ip", "is_correct": False}
        ]
    },
    {
        "text": "What is the default firewall management tool in Ubuntu Server?",
        "explanation": "UFW (Uncomplicated Firewall) is the default firewall management tool in Ubuntu, providing a user-friendly interface to iptables.",
        "reference": "https://ubuntu.com/server/docs/security-firewall",
        "points": 1,
        "answers": [
            {"text": "iptables", "is_correct": False},
            {"text": "ufw", "is_correct": True},
            {"text": "firewalld", "is_correct": False},
            {"text": "nftables", "is_correct": False}
        ]
    },
    {
        "text": "Which service management system does Ubuntu Server use?",
        "explanation": "Ubuntu Server uses systemd as its init system and service manager for controlling system services and processes.",
        "reference": "https://ubuntu.com/server/docs/service-management",
        "points": 1,
        "answers": [
            {"text": "SysV init", "is_correct": False},
            {"text": "systemd", "is_correct": True},
            {"text": "Upstart", "is_correct": False},
            {"text": "OpenRC", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Ubuntu Advantage (UA) for Infrastructure?",
        "explanation": "Ubuntu Advantage provides enterprise support, security updates, compliance tools, and additional services for Ubuntu deployments.",
        "reference": "https://ubuntu.com/advantage",
        "points": 1,
        "answers": [
            {"text": "Package repository", "is_correct": False},
            {"text": "Enterprise support and services", "is_correct": True},
            {"text": "Container platform", "is_correct": False},
            {"text": "Development framework", "is_correct": False}
        ]
    }
]
