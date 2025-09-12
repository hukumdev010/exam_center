"""Project Management Certifications Module"""

from . import (
    pmp,
    certified_scrummaster_csm,
    capm,
    pspo,
    pmi_acp,
    prince2_foundation,
    prince2_practitioner,
    cspo,
    safe_scrum_master
)

# Collect all Project Management certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    pmp,
    certified_scrummaster_csm,
    capm,
    pspo,
    pmi_acp,
    prince2_foundation,
    prince2_practitioner,
    cspo,
    safe_scrum_master
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']