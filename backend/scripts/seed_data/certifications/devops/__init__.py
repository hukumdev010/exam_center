"""DevOps Certifications Module"""

from . import (
    docker_certified_associate,
    certified_kubernetes_administrator_cka
)

# Collect all DevOps certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    docker_certified_associate,
    certified_kubernetes_administrator_cka
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']