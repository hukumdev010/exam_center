"""Information Technology Certifications Module"""

import importlib

# Collect all IT certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# List of module names to try importing
module_names = [
    'aws',
    'azure',
    'cybersecurity',
    'data_analytics',
    'data_structures_algorithms',
    'database',
    'devops',
    'google_cloud',
    'linux',
    'networking',
    'programming',
    'project_management',
    'system_design',
]

# Import certifications and questions from all available modules
for module_name in module_names:
    try:
        module = importlib.import_module(f'.{module_name}', package=__name__)
        if hasattr(module, 'CERTIFICATIONS'):
            CERTIFICATIONS.extend(module.CERTIFICATIONS)
        if hasattr(module, 'ALL_QUESTIONS'):
            ALL_QUESTIONS.update(module.ALL_QUESTIONS)
    except ImportError:
        # Skip modules that can't be imported
        continue