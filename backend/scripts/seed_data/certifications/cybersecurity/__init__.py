"""Cybersecurity Certifications Module"""

from . import (
    comptia_security_plus,
    certified_ethical_hacker,
    cisa,
    cism,
    cissp,
    comptia_cysa_plus,
    comptia_pentest_plus,
    giac_gsec,
    ciscp_professional,
    comptia_casp_plus,
    giac_gcih,
    giac_gcfa,
    comptia_network_plus_security,
    oscp_offensive_security
)

# Collect all Cybersecurity certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [
    comptia_security_plus,
    certified_ethical_hacker,
    cisa,
    cism,
    cissp,
    comptia_cysa_plus,
    comptia_pentest_plus,
    giac_gsec,
    ciscp_professional,
    comptia_casp_plus,
    giac_gcih,
    giac_gcfa,
    comptia_network_plus_security,
    oscp_offensive_security
]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']
