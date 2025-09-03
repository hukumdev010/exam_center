"""Azure Certifications Module"""

from . import (
    fundamentals_az900, 
    solutions_architect_expert,
    developer_associate_az204,
    administrator_associate_az104,
    security_engineer_associate_az500,
    devops_engineer_expert_az400,
    data_scientist_associate_dp100,
    data_engineer_associate_dp203,
    database_administrator_associate_dp300,
    ai_engineer_associate_ai102
)

# Collect all Azure certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    fundamentals_az900, 
    solutions_architect_expert,
    developer_associate_az204,
    administrator_associate_az104,
    security_engineer_associate_az500,
    devops_engineer_expert_az400,
    data_scientist_associate_dp100,
    data_engineer_associate_dp203,
    database_administrator_associate_dp300,
    ai_engineer_associate_ai102
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']