"""Azure Data Scientist Associate Certification"""

CERTIFICATION = {
    "name": "Azure Data Scientist Associate",
    "description": "Apply data science techniques on Azure",
    "slug": "azure-data-scientist-associate-dp100",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "azure",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Azure service is the primary platform for machine learning model development and deployment?",
        "explanation": "Azure Machine Learning is a cloud service for accelerating and managing the machine learning project lifecycle, including model training, deployment, and management.",
        "reference": "https://docs.microsoft.com/en-us/azure/machine-learning/",
        "points": 1,
        "answers": [
            {"text": "Azure Cognitive Services", "is_correct": False},
            {"text": "Azure Machine Learning", "is_correct": True},
            {"text": "Azure Databricks", "is_correct": False},
            {"text": "Azure HDInsight", "is_correct": False},
        ],
    },
    {
        "text": "What is AutoML in Azure Machine Learning?",
        "explanation": "AutoML (Automated Machine Learning) in Azure Machine Learning automates the process of algorithm selection, hyperparameter tuning, and feature engineering to build high-quality machine learning models.",
        "reference": "https://docs.microsoft.com/en-us/azure/machine-learning/concept-automated-ml",
        "points": 1,
        "answers": [
            {"text": "Manual model optimization", "is_correct": False},
            {
                "text": "Automated machine learning model development",
                "is_correct": True,
            },
            {"text": "Automatic data collection", "is_correct": False},
            {"text": "Automated deployment scaling", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides managed Jupyter notebooks for data science?",
        "explanation": "Azure Machine Learning provides managed compute instances with Jupyter notebooks, along with pre-installed data science tools and frameworks for collaborative data science work.",
        "reference": "https://docs.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks",
        "points": 1,
        "answers": [
            {"text": "Azure Notebooks (deprecated)", "is_correct": False},
            {"text": "Azure Machine Learning compute instances", "is_correct": True},
            {"text": "Azure Container Instances", "is_correct": False},
            {"text": "Azure Virtual Machines", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Machine Learning Model Registry used for?",
        "explanation": "The Model Registry in Azure Machine Learning is used to store, version, and manage machine learning models throughout their lifecycle, providing metadata tracking and model governance.",
        "reference": "https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment",
        "points": 1,
        "answers": [
            {"text": "Storing training data", "is_correct": False},
            {"text": "Managing and versioning ML models", "is_correct": True},
            {"text": "Monitoring model performance", "is_correct": False},
            {"text": "Scheduling training jobs", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides Apache Spark-based analytics specifically optimized for data science?",
        "explanation": "Azure Databricks is an Apache Spark-based analytics platform optimized for Azure, providing collaborative workspace for data scientists, data engineers, and business analysts.",
        "reference": "https://docs.microsoft.com/en-us/azure/databricks/",
        "points": 1,
        "answers": [
            {"text": "Azure HDInsight", "is_correct": False},
            {"text": "Azure Databricks", "is_correct": True},
            {"text": "Azure Synapse Analytics", "is_correct": False},
            {"text": "Azure Data Factory", "is_correct": False},
        ],
    },
]
