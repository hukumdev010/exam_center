"""Data Analytics Certifications Module"""

from . import (
    apache_spark_developer,
    google_analytics_certified,
    google_cloud_data_engineer,
    microsoft_power_bi,
    qlik_sense_data_architect,
    sas_statistical_business_analyst,
    tableau_desktop_specialist,
)

# Collect all Data Analytics certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    google_analytics_certified,
    microsoft_power_bi,
    tableau_desktop_specialist,
    sas_statistical_business_analyst,
    google_cloud_data_engineer,
    apache_spark_developer,
    qlik_sense_data_architect,
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, "QUESTIONS") and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION["slug"]] = module.QUESTIONS

__all__ = ["CERTIFICATIONS", "ALL_QUESTIONS"]
