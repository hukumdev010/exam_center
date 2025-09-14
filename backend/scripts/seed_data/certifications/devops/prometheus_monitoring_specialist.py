"""Prometheus Monitoring Specialist Certification"""

CERTIFICATION = {
    "name": "Prometheus Monitoring Specialist",
    "description": "Prometheus monitoring, alerting, and observability platform expertise",
    "slug": "prometheus-monitoring-specialist",
    "level": "Specialist",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "devops",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Prometheus?",
        "explanation": "Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects metrics from configured targets at given intervals and can trigger alerts when certain conditions are met.",
        "reference": "https://prometheus.io/docs/introduction/overview/",
        "points": 1,
        "answers": [
            {
                "text": "An open-source monitoring and alerting toolkit",
                "is_correct": True,
            },
            {"text": "A container orchestration platform", "is_correct": False},
            {"text": "A version control system", "is_correct": False},
            {"text": "A CI/CD pipeline tool", "is_correct": False},
        ],
    },
    {
        "text": "What is PromQL?",
        "explanation": "PromQL (Prometheus Query Language) is a functional query language that lets you select and aggregate time series data in real time. It's used to query metrics stored in Prometheus.",
        "reference": "https://prometheus.io/docs/prometheus/latest/querying/basics/",
        "points": 1,
        "answers": [
            {
                "text": "Prometheus Query Language for selecting and aggregating metrics",
                "is_correct": True,
            },
            {
                "text": "A programming language for writing monitoring scripts",
                "is_correct": False,
            },
            {"text": "A configuration file format", "is_correct": False},
            {"text": "A database schema language", "is_correct": False},
        ],
    },
    {
        "text": "What is a Prometheus scrape target?",
        "explanation": "A scrape target is an endpoint that Prometheus pulls (scrapes) metrics from. Targets are typically applications or services that expose metrics in Prometheus format at an HTTP endpoint.",
        "reference": "https://prometheus.io/docs/prometheus/latest/configuration/configuration/",
        "points": 1,
        "answers": [
            {
                "text": "An endpoint that Prometheus pulls metrics from",
                "is_correct": True,
            },
            {"text": "A backup storage location", "is_correct": False},
            {"text": "A user interface component", "is_correct": False},
            {"text": "A log file destination", "is_correct": False},
        ],
    },
    {
        "text": "What is Grafana's relationship to Prometheus?",
        "explanation": "Grafana is a popular visualization tool that can use Prometheus as a data source to create dashboards and graphs. While Prometheus focuses on data collection and alerting, Grafana provides rich visualization capabilities.",
        "reference": "https://prometheus.io/docs/visualization/grafana/",
        "points": 1,
        "answers": [
            {
                "text": "Grafana visualizes data from Prometheus through dashboards",
                "is_correct": True,
            },
            {"text": "Grafana replaces Prometheus", "is_correct": False},
            {"text": "Grafana is part of Prometheus", "is_correct": False},
            {"text": "They are competing products", "is_correct": False},
        ],
    },
    {
        "text": "What is Alertmanager in the Prometheus ecosystem?",
        "explanation": "Alertmanager handles alerts sent by Prometheus server. It takes care of deduplicating, grouping, and routing alerts to the correct receiver integrations such as email, PagerDuty, or Slack.",
        "reference": "https://prometheus.io/docs/alerting/latest/alertmanager/",
        "points": 1,
        "answers": [
            {
                "text": "Handles alert deduplication, grouping, and routing",
                "is_correct": True,
            },
            {"text": "Generates metrics data", "is_correct": False},
            {"text": "Creates visualization dashboards", "is_correct": False},
            {"text": "Stores long-term metrics", "is_correct": False},
        ],
    },
]
