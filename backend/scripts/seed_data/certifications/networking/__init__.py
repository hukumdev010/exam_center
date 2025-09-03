"""Networking Certifications Module"""

from . import (
    cisco_ccna,
    cisco_ccnp,
    comptia_network_plus,
    juniper_jncia,
    cissp_network_security
)

# Collect all Networking certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    cisco_ccna,
    cisco_ccnp,
    comptia_network_plus,
    juniper_jncia,
    cissp_network_security
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']