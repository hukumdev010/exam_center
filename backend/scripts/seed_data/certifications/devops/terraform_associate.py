"""Terraform Associate Certification"""

CERTIFICATION = {
    "name": "HashiCorp Certified: Terraform Associate",
    "description": "Infrastructure as Code using Terraform for cloud resource management",
    "slug": "terraform-associate",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "devops",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Infrastructure as Code (IaC)?",
        "explanation": "Infrastructure as Code is the practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.",
        "reference": "https://www.terraform.io/intro",
        "points": 1,
        "answers": [
            {
                "text": "Managing infrastructure through machine-readable definition files",
                "is_correct": True,
            },
            {
                "text": "Writing application code for infrastructure",
                "is_correct": False,
            },
            {"text": "Manually configuring servers", "is_correct": False},
            {"text": "Using only graphical interfaces", "is_correct": False},
        ],
    },
    {
        "text": "What is the Terraform state file?",
        "explanation": "The Terraform state file (terraform.tfstate) keeps track of the resources Terraform manages and their current state. It maps real-world resources to your configuration and tracks metadata.",
        "reference": "https://www.terraform.io/language/state",
        "points": 1,
        "answers": [
            {
                "text": "A file that tracks managed resources and their current state",
                "is_correct": True,
            },
            {
                "text": "A configuration file for Terraform settings",
                "is_correct": False,
            },
            {"text": "A backup of infrastructure code", "is_correct": False},
            {"text": "A log file of Terraform operations", "is_correct": False},
        ],
    },
    {
        "text": "What does 'terraform plan' do?",
        "explanation": "The 'terraform plan' command creates an execution plan, showing what actions Terraform will take to change your infrastructure to match the configuration without actually applying those changes.",
        "reference": "https://www.terraform.io/cli/commands/plan",
        "points": 1,
        "answers": [
            {
                "text": "Creates an execution plan showing proposed changes",
                "is_correct": True,
            },
            {"text": "Applies changes to infrastructure", "is_correct": False},
            {"text": "Destroys all resources", "is_correct": False},
            {"text": "Validates syntax only", "is_correct": False},
        ],
    },
    {
        "text": "What is a Terraform provider?",
        "explanation": "A provider is a plugin that Terraform uses to create and manage resources. Providers are responsible for understanding API interactions and exposing resources for specific services like AWS, Azure, or Google Cloud.",
        "reference": "https://www.terraform.io/language/providers",
        "points": 1,
        "answers": [
            {
                "text": "A plugin that manages resources for specific services",
                "is_correct": True,
            },
            {"text": "A user who provides Terraform code", "is_correct": False},
            {"text": "A hosting service for Terraform", "is_correct": False},
            {"text": "A backup solution", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Terraform modules?",
        "explanation": "Modules are reusable packages of Terraform configuration that allow you to organize, encapsulate, and reuse configurations. They help in creating maintainable and shareable infrastructure code.",
        "reference": "https://www.terraform.io/language/modules",
        "points": 1,
        "answers": [
            {
                "text": "Reusable packages of configuration for code organization",
                "is_correct": True,
            },
            {"text": "Individual resource definitions", "is_correct": False},
            {"text": "Terraform installation packages", "is_correct": False},
            {"text": "Database schemas", "is_correct": False},
        ],
    },
]
