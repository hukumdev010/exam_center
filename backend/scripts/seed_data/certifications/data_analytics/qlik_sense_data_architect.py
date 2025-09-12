"""Qlik Sense Data Architect Certification"""

CERTIFICATION = {
    "name": "Qlik Sense Data Architect",
    "description": "Design and develop Qlik Sense applications and data models for business intelligence",
    "slug": "qlik-sense-data-architect",
    "level": "Professional",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "data-analytics",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the Qlik Associative Model?",
        "explanation": "The Qlik Associative Model allows users to freely search and explore data by maintaining associations between all data elements, enabling dynamic filtering and discovery without predefined drill-down paths.",
        "reference": "https://help.qlik.com/en-US/sense/November2023/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-associative-model.htm",
        "points": 1,
        "answers": [
            {"text": "A data model that maintains associations between all data elements", "is_correct": True},
            {"text": "A relational database structure", "is_correct": False},
            {"text": "A machine learning algorithm", "is_correct": False},
            {"text": "A visualization technique", "is_correct": False}
        ]
    },
    {
        "text": "Which function is used to load data in Qlik Sense scripts?",
        "explanation": "The LOAD statement is the primary function for loading data into Qlik Sense, allowing data to be read from various sources and transformed during the loading process.",
        "reference": "https://help.qlik.com/en-US/sense/November2023/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm",
        "points": 1,
        "answers": [
            {"text": "LOAD", "is_correct": True},
            {"text": "SELECT", "is_correct": False},
            {"text": "IMPORT", "is_correct": False},
            {"text": "GET", "is_correct": False}
        ]
    },
    {
        "text": "What is a synthetic key in Qlik Sense?",
        "explanation": "A synthetic key is automatically created by Qlik Sense when two or more tables share multiple common field names, potentially indicating data model issues that should be resolved.",
        "reference": "https://help.qlik.com/en-US/sense/November2023/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/synthetic-keys.htm",
        "points": 1,
        "answers": [
            {"text": "An automatically created key when tables share multiple common fields", "is_correct": True},
            {"text": "A manually created primary key", "is_correct": False},
            {"text": "An encrypted field", "is_correct": False},
            {"text": "A calculated dimension", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of the Set Analysis in Qlik Sense?",
        "explanation": "Set Analysis allows you to define a set of data different from the current selection, enabling calculations that ignore current selections or use alternative selection criteria.",
        "reference": "https://help.qlik.com/en-US/sense/November2023/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-analysis.htm",
        "points": 1,
        "answers": [
            {"text": "Define a set of data different from current selections for calculations", "is_correct": True},
            {"text": "Analyze user behavior", "is_correct": False},
            {"text": "Set up data connections", "is_correct": False},
            {"text": "Configure security settings", "is_correct": False}
        ]
    },
    {
        "text": "Which Qlik Sense feature provides data lineage and impact analysis?",
        "explanation": "The Data Manager and Data Model Viewer provide data lineage information showing how data flows through the application and the impact of changes on related objects.",
        "reference": "https://help.qlik.com/en-US/sense/November2023/Subsystems/Hub/Content/Sense_Hub/DataManager/data-manager.htm",
        "points": 1,
        "answers": [
            {"text": "Data Manager and Data Model Viewer", "is_correct": True},
            {"text": "Set Analysis", "is_correct": False},
            {"text": "Master Items", "is_correct": False},
            {"text": "Storytelling", "is_correct": False}
        ]
    }
]
