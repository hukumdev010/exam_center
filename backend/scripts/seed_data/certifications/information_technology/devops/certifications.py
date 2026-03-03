"""DevOps Certifications Data"""

from .ansible_automation_specialist import CERTIFICATION as ANSIBLE_CERT
from .azure_devops_engineer_expert import CERTIFICATION as AZURE_DEVOPS_CERT
from .certified_kubernetes_administrator_cka import CERTIFICATION as CKA_CERT
from .docker_certified_associate import CERTIFICATION as DOCKER_CERT
from .gitlab_cicd_associate import CERTIFICATION as GITLAB_CERT
from .jenkins_certified_engineer import CERTIFICATION as JENKINS_CERT
from .prometheus_monitoring_specialist import CERTIFICATION as PROMETHEUS_CERT
from .terraform_associate import CERTIFICATION as TERRAFORM_CERT

CERTIFICATIONS = [
    DOCKER_CERT,
    JENKINS_CERT,
    TERRAFORM_CERT,
    CKA_CERT,
    ANSIBLE_CERT,
    GITLAB_CERT,
    AZURE_DEVOPS_CERT,
    PROMETHEUS_CERT
]