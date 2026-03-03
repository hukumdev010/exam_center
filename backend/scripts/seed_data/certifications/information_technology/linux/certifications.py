"""Linux Certifications Data"""

from .comptia_linux_plus import CERTIFICATION as LINUX_PLUS_CERT
from .lpic_1 import CERTIFICATION as LPIC1_CERT
from .lpic_2 import CERTIFICATION as LPIC2_CERT
from .lpic_3 import CERTIFICATION as LPIC3_CERT
from .rhcsa import CERTIFICATION as RHCSA_CERT
from .rhce import CERTIFICATION as RHCE_CERT
from .lfcs import CERTIFICATION as LFCS_CERT
from .lfce import CERTIFICATION as LFCE_CERT
from .suse_cla import CERTIFICATION as SUSE_CLA_CERT
from .ubuntu_server_pro import CERTIFICATION as UBUNTU_PRO_CERT

CERTIFICATIONS = [
    LINUX_PLUS_CERT,
    LPIC1_CERT,
    LPIC2_CERT,
    LPIC3_CERT,
    RHCSA_CERT,
    RHCE_CERT,
    LFCS_CERT,
    LFCE_CERT,
    SUSE_CLA_CERT,
    UBUNTU_PRO_CERT
]