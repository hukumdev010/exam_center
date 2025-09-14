"""Azure DevOps Engineer Expert Certification"""

CERTIFICATION = {
    "name": "Microsoft Azure DevOps Engineer Expert",
    "description": "Azure DevOps services for CI/CD, infrastructure management, and collaboration",
    "slug": "azure-devops-engineer-expert",
    "level": "Expert",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "devops",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Azure DevOps?",
        "explanation": "Azure DevOps is a set of development tools and services from Microsoft that provides version control, reporting, requirements management, project management, automated builds, testing, and release management capabilities.",
        "reference": "https://docs.microsoft.com/en-us/azure/devops/",
        "points": 1,
        "answers": [
            {
                "text": "A set of development tools and services for the software development lifecycle",
                "is_correct": True,
            },
            {"text": "A cloud computing platform", "is_correct": False},
            {"text": "A database management system", "is_correct": False},
            {"text": "A container orchestration service", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Pipelines?",
        "explanation": "Azure Pipelines is a cloud service that you can use to automatically build and test your code project and make it available to other users. It supports any language and platform and can deploy to any cloud or on-premises environment.",
        "reference": "https://docs.microsoft.com/en-us/azure/devops/pipelines/",
        "points": 1,
        "answers": [
            {
                "text": "A cloud service for automated build, test, and deployment",
                "is_correct": True,
            },
            {"text": "A version control system", "is_correct": False},
            {"text": "A project management tool", "is_correct": False},
            {"text": "A code review platform", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between Build and Release pipelines in Azure DevOps?",
        "explanation": "Build pipelines are used to compile code, run tests, and produce artifacts, while Release pipelines take those artifacts and deploy them to various environments following defined deployment strategies.",
        "reference": "https://docs.microsoft.com/en-us/azure/devops/pipelines/release/",
        "points": 1,
        "answers": [
            {
                "text": "Build pipelines create artifacts; Release pipelines deploy them",
                "is_correct": True,
            },
            {
                "text": "Build pipelines are faster than Release pipelines",
                "is_correct": False,
            },
            {"text": "Release pipelines are deprecated", "is_correct": False},
            {"text": "They are exactly the same", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Repos?",
        "explanation": "Azure Repos provides Git repositories or Team Foundation Version Control (TFVC) for source control of your code. It includes features like pull requests, branch policies, and code reviews.",
        "reference": "https://docs.microsoft.com/en-us/azure/devops/repos/",
        "points": 1,
        "answers": [
            {
                "text": "Git repositories and version control for source code",
                "is_correct": True,
            },
            {"text": "A container registry", "is_correct": False},
            {"text": "A package management system", "is_correct": False},
            {"text": "A monitoring service", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Boards?",
        "explanation": "Azure Boards provides a suite of Agile tools to support planning and tracking work, code defects, and issues using Kanban and Scrum methods. It includes work items, backlogs, sprints, and queries.",
        "reference": "https://docs.microsoft.com/en-us/azure/devops/boards/",
        "points": 1,
        "answers": [
            {
                "text": "Agile tools for planning and tracking work using Kanban and Scrum",
                "is_correct": True,
            },
            {"text": "A deployment dashboard", "is_correct": False},
            {"text": "A code analysis tool", "is_correct": False},
            {"text": "A testing framework", "is_correct": False},
        ],
    },
]
