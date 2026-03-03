"""AWS Certifications Data"""

from .advanced_networking_specialty import (
    CERTIFICATION as ADVANCED_NETWORKING_CERT
)
from .cloud_practitioner import CERTIFICATION as CLOUD_PRACTITIONER_CERT
from .data_analytics_specialty import CERTIFICATION as DATA_ANALYTICS_CERT
from .database_specialty import CERTIFICATION as DATABASE_SPECIALTY_CERT
from .developer_associate import (
     CERTIFICATION as DEVELOPER_ASSOCIATE_CERT
)
from .devops_engineer_professional import (
    CERTIFICATION as DEVOPS_PROFESSIONAL_CERT
)
from .machine_learning_specialty import CERTIFICATION as ML_SPECIALTY_CERT
from .security_specialty import CERTIFICATION as SECURITY_SPECIALTY_CERT
from .solutions_architect_associate import CERTIFICATION as SA_ASSOCIATE_CERT
from .solutions_architect_professional import (
    CERTIFICATION as SA_PROFESSIONAL_CERT
)
from .sysops_administrator import CERTIFICATION as SYSOPS_ADMIN_CERT

CERTIFICATIONS = [
    CLOUD_PRACTITIONER_CERT,
    DEVELOPER_ASSOCIATE_CERT,
    SA_ASSOCIATE_CERT,
    SYSOPS_ADMIN_CERT,
    SA_PROFESSIONAL_CERT,
    DEVOPS_PROFESSIONAL_CERT,
    ADVANCED_NETWORKING_CERT,
    SECURITY_SPECIALTY_CERT,
    DATABASE_SPECIALTY_CERT,
    DATA_ANALYTICS_CERT,
    ML_SPECIALTY_CERT
]