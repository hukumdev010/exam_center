"""Data Structures & Algorithms Certifications Module"""

from . import (
    data_structures_fundamentals,
    algorithms_fundamentals,
    advanced_data_structures,
    advanced_algorithms,
    algorithm_design_analysis,
    competitive_programming
)

# Collect all Data Structures & Algorithms certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    data_structures_fundamentals,
    algorithms_fundamentals,
    advanced_data_structures,
    advanced_algorithms,
    algorithm_design_analysis,
    competitive_programming
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, 'QUESTIONS') and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION['slug']] = module.QUESTIONS

__all__ = ['CERTIFICATIONS', 'ALL_QUESTIONS']