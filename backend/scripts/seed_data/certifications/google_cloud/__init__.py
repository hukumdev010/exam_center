"""Google Cloud Certifications Module"""

from . import (
    associate_cloud_engineer,
    digital_leader,
    professional_cloud_architect,
    professional_cloud_network_engineer,
    professional_cloud_security_engineer,
    professional_data_engineer,
    professional_devops_engineer,
    professional_machine_learning_engineer,
)

# Collect all Google Cloud certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    digital_leader,
    associate_cloud_engineer,
    professional_cloud_architect,
    professional_data_engineer,
    professional_devops_engineer,
    professional_cloud_security_engineer,
    professional_cloud_network_engineer,
    professional_machine_learning_engineer,
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, "QUESTIONS") and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION["slug"]] = module.QUESTIONS

__all__ = ["CERTIFICATIONS", "ALL_QUESTIONS"]
