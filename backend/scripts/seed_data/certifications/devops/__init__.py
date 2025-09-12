"""DevOps Certifications Module"""

from . import (
    docker_certified_associate,
    certified_kubernetes_administrator_cka,
    jenkins_certified_engineer,
    terraform_associate,
    ansible_automation_specialist,
    gitlab_cicd_associate,
    prometheus_monitoring_specialist,
    azure_devops_engineer_expert
)

# Collect all DevOps certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    docker_certified_associate,
    certified_kubernetes_administrator_cka,
    jenkins_certified_engineer,
    terraform_associate,
    ansible_automation_specialist,
    gitlab_cicd_associate,
    prometheus_monitoring_specialist,
    azure_devops_engineer_expert
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']