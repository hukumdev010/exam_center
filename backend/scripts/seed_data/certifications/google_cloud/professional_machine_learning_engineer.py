"""Google Cloud Professional Machine Learning Engineer Certification"""

CERTIFICATION = {
    "name": "Google Cloud Professional Machine Learning Engineer",
    "description": "Design, build, and productionize machine learning models to solve business challenges using Google Cloud",
    "slug": "google-professional-machine-learning-engineer",
    "level": "Professional",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "google-cloud",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which Google Cloud service provides managed machine learning model training and deployment?",
        "explanation": "Vertex AI is Google Cloud's unified machine learning platform that provides tools for the entire ML workflow, from data preparation to model deployment.",
        "reference": "https://cloud.google.com/vertex-ai/docs",
        "points": 1,
        "answers": [
            {"text": "AI Platform", "is_correct": False},
            {"text": "Vertex AI", "is_correct": True},
            {"text": "AutoML", "is_correct": False},
            {"text": "BigQuery ML", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary purpose of BigQuery ML?",
        "explanation": "BigQuery ML enables users to create and execute machine learning models directly in BigQuery using SQL queries, without needing to move data out of the warehouse.",
        "reference": "https://cloud.google.com/bigquery-ml/docs",
        "points": 1,
        "answers": [
            {"text": "Data storage", "is_correct": False},
            {"text": "ML model creation using SQL", "is_correct": True},
            {"text": "Data visualization", "is_correct": False},
            {"text": "ETL processing", "is_correct": False}
        ]
    },
    {
        "text": "Which Google Cloud service provides pre-trained models for common AI tasks?",
        "explanation": "Cloud AI APIs offer pre-trained models for vision, language, translation, and other AI tasks, allowing developers to add AI capabilities without building models from scratch.",
        "reference": "https://cloud.google.com/ai/",
        "points": 1,
        "answers": [
            {"text": "Vertex AI", "is_correct": False},
            {"text": "Cloud AI APIs", "is_correct": True},
            {"text": "AutoML", "is_correct": False},
            {"text": "AI Notebooks", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of Kubeflow Pipelines in Google Cloud?",
        "explanation": "Kubeflow Pipelines is a platform for building and deploying portable, scalable machine learning workflows based on Docker containers.",
        "reference": "https://cloud.google.com/vertex-ai/docs/pipelines",
        "points": 1,
        "answers": [
            {"text": "Data storage", "is_correct": False},
            {"text": "ML workflow orchestration", "is_correct": True},
            {"text": "Model serving", "is_correct": False},
            {"text": "Feature engineering", "is_correct": False}
        ]
    },
    {
        "text": "Which Google Cloud service provides managed Jupyter notebooks for ML development?",
        "explanation": "Vertex AI Workbench (formerly AI Platform Notebooks) provides managed Jupyter notebook instances optimized for machine learning development and experimentation.",
        "reference": "https://cloud.google.com/vertex-ai/docs/workbench",
        "points": 1,
        "answers": [
            {"text": "Colab", "is_correct": False},
            {"text": "Vertex AI Workbench", "is_correct": True},
            {"text": "Datalab", "is_correct": False},
            {"text": "Cloud Shell", "is_correct": False}
        ]
    }
]
