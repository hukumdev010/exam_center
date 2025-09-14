"""GitLab Certified CI/CD Associate Certification"""

CERTIFICATION = {
    "name": "GitLab Certified CI/CD Associate",
    "description": "GitLab CI/CD pipeline development, DevOps practices, and automation",
    "slug": "gitlab-cicd-associate",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "devops",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is GitLab CI/CD?",
        "explanation": "GitLab CI/CD is a built-in continuous integration and continuous deployment tool that allows you to automatically build, test, and deploy your code based on triggers like commits, merge requests, or schedules.",
        "reference": "https://docs.gitlab.com/ee/ci/",
        "points": 1,
        "answers": [
            {
                "text": "A built-in tool for automated build, test, and deployment",
                "is_correct": True,
            },
            {"text": "A version control system", "is_correct": False},
            {"text": "A project management tool", "is_correct": False},
            {"text": "A code review platform", "is_correct": False},
        ],
    },
    {
        "text": "What file defines GitLab CI/CD pipelines?",
        "explanation": "The .gitlab-ci.yml file placed in the root of your repository defines the CI/CD pipeline configuration, including jobs, stages, and scripts to be executed.",
        "reference": "https://docs.gitlab.com/ee/ci/yaml/",
        "points": 1,
        "answers": [
            {"text": ".gitlab-ci.yml", "is_correct": True},
            {"text": "Dockerfile", "is_correct": False},
            {"text": "pipeline.json", "is_correct": False},
            {"text": "config.yaml", "is_correct": False},
        ],
    },
    {
        "text": "What is a GitLab Runner?",
        "explanation": "A GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline. Runners can be installed on different machines and can execute jobs in various environments.",
        "reference": "https://docs.gitlab.com/runner/",
        "points": 1,
        "answers": [
            {"text": "An application that executes CI/CD jobs", "is_correct": True},
            {"text": "A user with special permissions", "is_correct": False},
            {"text": "A backup system", "is_correct": False},
            {"text": "A monitoring tool", "is_correct": False},
        ],
    },
    {
        "text": "What are GitLab CI/CD stages?",
        "explanation": "Stages define the order of execution for jobs in a pipeline. Jobs in the same stage run in parallel, while stages run sequentially. Common stages include build, test, and deploy.",
        "reference": "https://docs.gitlab.com/ee/ci/yaml/#stages",
        "points": 1,
        "answers": [
            {
                "text": "Groups of jobs that define execution order in pipelines",
                "is_correct": True,
            },
            {"text": "Different environments for deployment", "is_correct": False},
            {"text": "User permission levels", "is_correct": False},
            {"text": "Git branch types", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of GitLab CI/CD variables?",
        "explanation": "CI/CD variables allow you to pass configuration and sensitive data to jobs without hardcoding them in your .gitlab-ci.yml file. They can be defined at project, group, or instance level.",
        "reference": "https://docs.gitlab.com/ee/ci/variables/",
        "points": 1,
        "answers": [
            {
                "text": "Pass configuration and sensitive data to jobs securely",
                "is_correct": True,
            },
            {"text": "Store git commit messages", "is_correct": False},
            {"text": "Define user permissions", "is_correct": False},
            {"text": "Configure GitLab server settings", "is_correct": False},
        ],
    },
]
