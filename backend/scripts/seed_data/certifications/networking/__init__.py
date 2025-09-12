"""Networking Certifications Module"""

from . import (
    cisco_ccna,
    cisco_ccnp,
    cisco_ccie,
    comptia_network_plus,
    juniper_jncia,
    juniper_jncip,
    cissp_network_security,
    palo_alto_pcnse,
    fortinet_nse,
    wireshark_wcna
)

# Collect all Networking certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    cisco_ccna,
    cisco_ccnp,
    cisco_ccie,
    comptia_network_plus,
    juniper_jncia,
    juniper_jncip,
    cissp_network_security,
    palo_alto_pcnse,
    fortinet_nse,
    wireshark_wcna
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']