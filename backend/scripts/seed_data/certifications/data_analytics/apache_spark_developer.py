"""Apache Spark Developer Certification"""

CERTIFICATION = {
    "name": "Apache Spark Developer Certification",
    "description": "Develop and optimize big data applications using Apache Spark for distributed computing",
    "slug": "apache-spark-developer",
    "level": "Intermediate",
    "duration": 90,
    "questions_count": 40,
    "category_slug": "data-analytics",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the fundamental data structure in Apache Spark?",
        "explanation": "RDD (Resilient Distributed Dataset) is the fundamental data structure in Apache Spark, representing an immutable, distributed collection of objects that can be processed in parallel.",
        "reference": "https://spark.apache.org/docs/latest/rdd-programming-guide.html",
        "points": 1,
        "answers": [
            {"text": "RDD (Resilient Distributed Dataset)", "is_correct": True},
            {"text": "DataFrame", "is_correct": False},
            {"text": "Dataset", "is_correct": False},
            {"text": "Array", "is_correct": False}
        ]
    },
    {
        "text": "Which Spark component is used for SQL queries?",
        "explanation": "Spark SQL is the module for working with structured data using SQL queries, DataFrames, and Datasets, providing a programming abstraction and optimized execution engine.",
        "reference": "https://spark.apache.org/docs/latest/sql-programming-guide.html",
        "points": 1,
        "answers": [
            {"text": "Spark SQL", "is_correct": True},
            {"text": "Spark Streaming", "is_correct": False},
            {"text": "MLlib", "is_correct": False},
            {"text": "GraphX", "is_correct": False}
        ]
    },
    {
        "text": "What is the difference between transformations and actions in Spark?",
        "explanation": "Transformations are lazy operations that define a new RDD from existing ones (like map, filter), while actions trigger computation and return results (like collect, count, save).",
        "reference": "https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-operations",
        "points": 1,
        "answers": [
            {"text": "Transformations are lazy; actions trigger computation", "is_correct": True},
            {"text": "Transformations are faster than actions", "is_correct": False},
            {"text": "Actions are lazy; transformations trigger computation", "is_correct": False},
            {"text": "They are the same thing", "is_correct": False}
        ]
    },
    {
        "text": "Which storage level persists RDDs in memory?",
        "explanation": "MEMORY_ONLY storage level caches RDDs in the JVM heap memory as deserialized Java objects, providing the fastest access but using more memory.",
        "reference": "https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence",
        "points": 1,
        "answers": [
            {"text": "MEMORY_ONLY", "is_correct": True},
            {"text": "DISK_ONLY", "is_correct": False},
            {"text": "NONE", "is_correct": False},
            {"text": "MEMORY_AND_DISK_SER", "is_correct": False}
        ]
    },
    {
        "text": "What is a Spark DataFrame?",
        "explanation": "A DataFrame is a distributed collection of data organized into named columns, similar to a table in a relational database, built on top of RDDs with schema information and optimizations.",
        "reference": "https://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes",
        "points": 1,
        "answers": [
            {"text": "A distributed collection of data organized into named columns", "is_correct": True},
            {"text": "A single machine data structure", "is_correct": False},
            {"text": "A configuration file", "is_correct": False},
            {"text": "A machine learning model", "is_correct": False}
        ]
    }
]
