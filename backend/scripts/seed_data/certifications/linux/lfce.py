"""Linux Foundation Certified Engineer (LFCE)"""

CERTIFICATION = {
    "name": "Linux Foundation Certified Engineer (LFCE)",
    "description": "Advanced Linux engineering and enterprise system administration",
    "slug": "lfce",
    "level": "Expert",
    "duration": 120,
    "questions_count": 20,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which tool is commonly used for configuration management and automation in Linux environments?",
        "explanation": "Ansible is a popular configuration management tool that uses YAML playbooks to automate system configuration and deployment tasks.",
        "reference": "https://training.linuxfoundation.org/certification/linux-foundation-certified-engineer-lfce/",
        "points": 1,
        "answers": [
            {"text": "Ansible", "is_correct": True},
            {"text": "grep", "is_correct": False},
            {"text": "vim", "is_correct": False},
            {"text": "cron", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary purpose of HAProxy in Linux infrastructure?",
        "explanation": "HAProxy is a high-performance load balancer and proxy server used for distributing incoming requests across multiple backend servers.",
        "reference": "https://www.haproxy.org/download/1.8/doc/configuration.txt",
        "points": 1,
        "answers": [
            {"text": "Database management", "is_correct": False},
            {"text": "Load balancing and proxying", "is_correct": True},
            {"text": "File system encryption", "is_correct": False},
            {"text": "User authentication", "is_correct": False}
        ]
    },
    {
        "text": "Which command is used to create and manage Linux containers with Docker?",
        "explanation": "The docker command-line interface is used to create, manage, and interact with Docker containers and images.",
        "reference": "https://docs.docker.com/engine/reference/commandline/docker/",
        "points": 1,
        "answers": [
            {"text": "container", "is_correct": False},
            {"text": "docker", "is_correct": True},
            {"text": "lxc", "is_correct": False},
            {"text": "podman", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Kubernetes in container orchestration?",
        "explanation": "Kubernetes is a container orchestration platform that automates deployment, scaling, and management of containerized applications.",
        "reference": "https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/",
        "points": 1,
        "answers": [
            {"text": "Web server hosting", "is_correct": False},
            {"text": "Container orchestration and management", "is_correct": True},
            {"text": "Database administration", "is_correct": False},
            {"text": "Network monitoring", "is_correct": False}
        ]
    },
    {
        "text": "Which monitoring solution is commonly used for metrics collection in Linux systems?",
        "explanation": "Prometheus is a popular open-source monitoring and alerting system designed for reliability and scalability in dynamic environments.",
        "reference": "https://prometheus.io/docs/introduction/overview/",
        "points": 1,
        "answers": [
            {"text": "Apache", "is_correct": False},
            {"text": "Prometheus", "is_correct": True},
            {"text": "MySQL", "is_correct": False},
            {"text": "Redis", "is_correct": False}
        ]
    }
]
