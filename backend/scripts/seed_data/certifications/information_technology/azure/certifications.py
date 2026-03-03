"""Azure Certifications Data"""

from .fundamentals_az900 import CERTIFICATION as AZ900_CERT
from .administrator_associate_az104 import CERTIFICATION as AZ104_CERT
from .developer_associate_az204 import CERTIFICATION as AZ204_CERT
from .security_engineer_associate_az500 import CERTIFICATION as AZ500_CERT
from .devops_engineer_expert_az400 import CERTIFICATION as AZ400_CERT
from .solutions_architect_expert import CERTIFICATION as SA_EXPERT_CERT
from .ai_engineer_associate_ai102 import CERTIFICATION as AI102_CERT
from .data_scientist_associate_dp100 import CERTIFICATION as DP100_CERT
from .data_engineer_associate_dp203 import CERTIFICATION as DP203_CERT
from .database_administrator_associate_dp300 import CERTIFICATION as DP300_CERT

CERTIFICATIONS = [
    AZ900_CERT,
    AZ104_CERT,
    AZ204_CERT,
    AZ500_CERT,
    AZ400_CERT,
    SA_EXPERT_CERT,
    AI102_CERT,
    DP100_CERT,
    DP203_CERT,
    DP300_CERT
]