"""Project Management Certifications Data"""

from .pmp import CERTIFICATION as PMP_CERT
from .capm import CERTIFICATION as CAPM_CERT
from .pmi_acp import CERTIFICATION as PMI_ACP_CERT
from .certified_scrummaster_csm import CERTIFICATION as CSM_CERT
from .cspo import CERTIFICATION as CSPO_CERT
from .pspo import CERTIFICATION as PSPO_CERT
from .safe_scrum_master import CERTIFICATION as SAFE_SM_CERT
from .prince2_foundation import CERTIFICATION as PRINCE2_FOUND_CERT
from .prince2_practitioner import CERTIFICATION as PRINCE2_PRAC_CERT

CERTIFICATIONS = [
    CAPM_CERT,
    PMP_CERT,
    PMI_ACP_CERT,
    CSM_CERT,
    CSPO_CERT,
    PSPO_CERT,
    SAFE_SM_CERT,
    PRINCE2_FOUND_CERT,
    PRINCE2_PRAC_CERT
]