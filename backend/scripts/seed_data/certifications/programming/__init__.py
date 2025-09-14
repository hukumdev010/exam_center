"""Programming Certifications Module"""

from . import (
    advanced_typescript,
    csharp_programming,
    go_programming,
    javascript_developer,
    nodejs_developer,
    oracle_java_se11_programmer_1,
    oracle_java_se11_programmer_2,
    python_pcap,
    python_pcep,
    react_developer,
    rust_programming,
    typescript_developer,
)

# Collect all Programming certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    python_pcep,
    python_pcap,
    oracle_java_se11_programmer_1,
    oracle_java_se11_programmer_2,
    javascript_developer,
    react_developer,
    nodejs_developer,
    csharp_programming,
    go_programming,
    rust_programming,
    typescript_developer,
    advanced_typescript,
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, "QUESTIONS") and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION["slug"]] = module.QUESTIONS

__all__ = ["CERTIFICATIONS", "ALL_QUESTIONS"]
