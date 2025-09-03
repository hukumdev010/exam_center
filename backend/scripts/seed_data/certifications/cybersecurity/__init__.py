"""Cybersecurity Certifications Module"""

from . import comptia_security_plus, certified_ethical_hacker

# Collect all Cybersecurity certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [comptia_security_plus, certified_ethical_hacker]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']
