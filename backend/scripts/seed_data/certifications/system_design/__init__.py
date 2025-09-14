"""System Design Certifications Module"""

from . import fundamentals, high_performance_architecture, microservices_architecture

# Collect all System Design certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [fundamentals, microservices_architecture, high_performance_architecture]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, "QUESTIONS") and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION["slug"]] = module.QUESTIONS

__all__ = ["CERTIFICATIONS", "ALL_QUESTIONS"]
