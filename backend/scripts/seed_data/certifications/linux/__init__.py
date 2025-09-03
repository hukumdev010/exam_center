"""Linux Certifications Module"""

from . import comptia_linux_plus, rhcsa, rhce, lpic_1

# Collect all Linux certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [comptia_linux_plus, rhcsa, rhce, lpic_1]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']
