"""Data Analytics Certifications Module"""

from . import (
    google_analytics_certified,
    microsoft_power_bi,
    tableau_desktop_specialist,
    sas_statistical_business_analyst,
    google_cloud_data_engineer,
    apache_spark_developer,
    qlik_sense_data_architect
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
    qlik_sense_data_architect
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']