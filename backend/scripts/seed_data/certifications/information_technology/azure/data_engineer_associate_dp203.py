"""Azure Data Engineer Associate Certification"""

CERTIFICATION = {
    "name": "Azure Data Engineer Associate",
    "description": "Design and implement data storage solutions on Azure",
    "slug": "azure-data-engineer-associate-dp203",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "azure",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Azure service is designed for big data analytics and data warehousing?",
        "explanation": "Azure Synapse Analytics (formerly SQL Data Warehouse) is a limitless analytics service that brings together data integration, data warehousing, and big data analytics in a unified experience.",
        "reference": "https://docs.microsoft.com/en-us/azure/synapse-analytics/",
        "points": 1,
        "answers": [
            {"text": "Azure SQL Database", "is_correct": False},
            {"text": "Azure Synapse Analytics", "is_correct": True},
            {"text": "Azure Cosmos DB", "is_correct": False},
            {"text": "Azure Table Storage", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Data Factory primarily used for?",
        "explanation": "Azure Data Factory is a cloud-based data integration service that orchestrates and automates the movement and transformation of data between various data stores and compute services.",
        "reference": "https://docs.microsoft.com/en-us/azure/data-factory/",
        "points": 1,
        "answers": [
            {"text": "Data storage", "is_correct": False},
            {"text": "Data integration and ETL processes", "is_correct": True},
            {"text": "Machine learning model training", "is_correct": False},
            {"text": "Real-time data streaming", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides real-time analytics on streaming data?",
        "explanation": "Azure Stream Analytics is a real-time analytics service designed to analyze and process fast streaming data from multiple sources simultaneously, enabling real-time decision making.",
        "reference": "https://docs.microsoft.com/en-us/azure/stream-analytics/",
        "points": 1,
        "answers": [
            {"text": "Azure Data Lake", "is_correct": False},
            {"text": "Azure Stream Analytics", "is_correct": True},
            {"text": "Azure Data Factory", "is_correct": False},
            {"text": "Azure HDInsight", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Azure Data Lake Storage?",
        "explanation": "Azure Data Lake Storage is a scalable data storage and analytics service that provides a massively scalable and secure data lake for high-performance analytics workloads.",
        "reference": "https://docs.microsoft.com/en-us/azure/storage/data-lake-storage/",
        "points": 1,
        "answers": [
            {"text": "Relational database storage", "is_correct": False},
            {"text": "Massively scalable data lake for analytics", "is_correct": True},
            {"text": "Key-value pair storage", "is_correct": False},
            {"text": "Document database storage", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service is used for Apache Spark-based analytics?",
        "explanation": "Azure HDInsight provides managed Apache Spark clusters in the cloud, enabling big data analytics and machine learning workloads. Azure Synapse Analytics also includes Apache Spark pools.",
        "reference": "https://docs.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-overview",
        "points": 1,
        "answers": [
            {"text": "Azure Functions", "is_correct": False},
            {"text": "Azure HDInsight", "is_correct": True},
            {"text": "Azure Logic Apps", "is_correct": False},
            {"text": "Azure Service Bus", "is_correct": False},
        ],
    },
]
