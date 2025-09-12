"""AWS Certifications Module"""

from . import (
    cloud_practitioner, 
    solutions_architect_associate, 
    solutions_architect_professional, 
    developer_associate, 
    security_specialty,
    sysops_administrator,
    data_analytics_specialty,
    machine_learning_specialty,
    devops_engineer_professional,
    advanced_networking_specialty,
    database_specialty
)

# Collect all AWS certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [
    cloud_practitioner, 
    solutions_architect_associate, 
    solutions_architect_professional, 
    developer_associate, 
    security_specialty,
    sysops_administrator,
    data_analytics_specialty,
    machine_learning_specialty,
    devops_engineer_professional,
    advanced_networking_specialty,
    database_specialty
]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']
