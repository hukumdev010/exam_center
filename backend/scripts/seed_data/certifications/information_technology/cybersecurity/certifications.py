"""Cybersecurity Certifications Data"""

from .comptia_security_plus import CERTIFICATION as SECURITY_PLUS_CERT
from .comptia_cysa_plus import CERTIFICATION as CYSA_PLUS_CERT
from .comptia_pentest_plus import CERTIFICATION as PENTEST_PLUS_CERT
from .comptia_casp_plus import CERTIFICATION as CASP_PLUS_CERT
from .comptia_network_plus_security import CERTIFICATION as NETWORK_PLUS_CERT
from .certified_ethical_hacker import CERTIFICATION as CEH_CERT
from .cissp import CERTIFICATION as CISSP_CERT
from .cism import CERTIFICATION as CISM_CERT
from .cisa import CERTIFICATION as CISA_CERT
from .ciscp_professional import CERTIFICATION as CISCP_CERT
from .oscp_offensive_security import CERTIFICATION as OSCP_CERT
from .giac_gsec import CERTIFICATION as GIAC_GSEC_CERT
from .giac_gcih import CERTIFICATION as GIAC_GCIH_CERT
from .giac_gcfa import CERTIFICATION as GIAC_GCFA_CERT

CERTIFICATIONS = [
    SECURITY_PLUS_CERT,
    CYSA_PLUS_CERT,
    PENTEST_PLUS_CERT,
    CASP_PLUS_CERT,
    NETWORK_PLUS_CERT,
    CEH_CERT,
    CISSP_CERT,
    CISM_CERT,
    CISA_CERT,
    CISCP_CERT,
    OSCP_CERT,
    GIAC_GSEC_CERT,
    GIAC_GCIH_CERT,
    GIAC_GCFA_CERT
]

