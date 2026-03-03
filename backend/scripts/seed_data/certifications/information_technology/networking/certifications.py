"""Networking Certifications Data"""

from .comptia_network_plus import CERTIFICATION as NETWORK_PLUS_CERT
from .cisco_ccna import CERTIFICATION as CCNA_CERT
from .cisco_ccnp import CERTIFICATION as CCNP_CERT
from .cisco_ccie import CERTIFICATION as CCIE_CERT
from .juniper_jncia import CERTIFICATION as JNCIA_CERT
from .juniper_jncip import CERTIFICATION as JNCIP_CERT
from .fortinet_nse import CERTIFICATION as NSE_CERT
from .palo_alto_pcnse import CERTIFICATION as PCNSE_CERT
from .cissp_network_security import CERTIFICATION as CISSP_NET_CERT
from .wireshark_wcna import CERTIFICATION as WCNA_CERT

CERTIFICATIONS = [
    NETWORK_PLUS_CERT,
    CCNA_CERT,
    CCNP_CERT,
    CCIE_CERT,
    JNCIA_CERT,
    JNCIP_CERT,
    NSE_CERT,
    PCNSE_CERT,
    CISSP_NET_CERT,
    WCNA_CERT
]