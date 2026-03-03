"""Data Analytics Certifications Data"""

from .tableau_desktop_specialist import CERTIFICATION as TABLEAU_CERT
from .microsoft_power_bi import CERTIFICATION as POWER_BI_CERT
from .google_analytics_certified import CERTIFICATION as GOOGLE_ANALYTICS_CERT
from .google_cloud_data_engineer import CERTIFICATION as GCP_DATA_ENGINEER_CERT
from .apache_spark_developer import CERTIFICATION as SPARK_DEVELOPER_CERT
from .qlik_sense_data_architect import CERTIFICATION as QLIK_SENSE_CERT
from .sas_statistical_business_analyst import CERTIFICATION as SAS_ANALYST_CERT

CERTIFICATIONS = [
    TABLEAU_CERT,
    POWER_BI_CERT,
    GOOGLE_ANALYTICS_CERT,
    GCP_DATA_ENGINEER_CERT,
    SPARK_DEVELOPER_CERT,
    QLIK_SENSE_CERT,
    SAS_ANALYST_CERT
]