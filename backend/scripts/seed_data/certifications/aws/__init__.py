"""AWS Certifications Module"""

from . import cloud_practitioner, solutions_architect_associate, solutions_architect_professional, developer_associate, security_specialty

# Collect all AWS certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [cloud_practitioner, solutions_architect_associate, solutions_architect_professional, developer_associate, security_specialty]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']
