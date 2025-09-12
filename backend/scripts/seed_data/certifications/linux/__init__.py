"""Linux Certifications Module"""

from . import (
    comptia_linux_plus, 
    rhcsa, 
    rhce, 
    lpic_1, 
    lpic_2, 
    lpic_3, 
    lfcs, 
    lfce, 
    suse_cla, 
    ubuntu_server_pro
)

# Collect all Linux certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
for module in [
    comptia_linux_plus, 
    rhcsa, 
    rhce, 
    lpic_1, 
    lpic_2, 
    lpic_3, 
    lfcs, 
    lfce, 
    suse_cla, 
    ubuntu_server_pro
]:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']
