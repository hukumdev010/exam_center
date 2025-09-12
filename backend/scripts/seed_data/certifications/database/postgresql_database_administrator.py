"""PostgreSQL Database Administrator Certification"""

CERTIFICATION = {
    "name": "PostgreSQL Database Administrator",
    "description": "PostgreSQL database administration, performance tuning, and advanced features",
    "slug": "postgresql-database-administrator",
    "level": "Professional",
    "duration": 120,
    "questions_count": 65,
    "category_slug": "database",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is MVCC in PostgreSQL?",
        "explanation": "Multi-Version Concurrency Control (MVCC) allows PostgreSQL to provide transaction isolation without locking. Each transaction sees a snapshot of data that is consistent with the state of the database at the start of the transaction.",
        "reference": "https://www.postgresql.org/docs/current/mvcc.html",
        "points": 1,
        "answers": [
            {"text": "Multi-Version Concurrency Control for transaction isolation", "is_correct": True},
            {"text": "Multiple Virtual Connection Controller", "is_correct": False},
            {"text": "Master-Validator Configuration Control", "is_correct": False},
            {"text": "Memory Variable Cache Control", "is_correct": False}
        ]
    },
    {
        "text": "Which PostgreSQL command is used to analyze query performance?",
        "explanation": "EXPLAIN ANALYZE executes the query and shows the actual time spent in each part of the query plan, providing detailed information about query performance and execution statistics.",
        "reference": "https://www.postgresql.org/docs/current/sql-explain.html",
        "points": 1,
        "answers": [
            {"text": "EXPLAIN ANALYZE", "is_correct": True},
            {"text": "SHOW PERFORMANCE", "is_correct": False},
            {"text": "ANALYZE QUERY", "is_correct": False},
            {"text": "PERFORMANCE SCHEMA", "is_correct": False}
        ]
    },
    {
        "text": "What is a PostgreSQL tablespace?",
        "explanation": "A tablespace defines a location in the file system where the files representing database objects can be stored. It allows administrators to control the disk layout of a PostgreSQL installation.",
        "reference": "https://www.postgresql.org/docs/current/manage-ag-tablespaces.html",
        "points": 1,
        "answers": [
            {"text": "A location in the file system for storing database files", "is_correct": True},
            {"text": "A temporary storage area for queries", "is_correct": False},
            {"text": "A memory allocation for connections", "is_correct": False},
            {"text": "A backup storage location", "is_correct": False}
        ]
    },
    {
        "text": "Which PostgreSQL feature provides automatic query optimization?",
        "explanation": "The PostgreSQL query planner (optimizer) automatically chooses the most efficient way to execute each query by analyzing the query structure, available indexes, and table statistics.",
        "reference": "https://www.postgresql.org/docs/current/planner-optimizer.html",
        "points": 1,
        "answers": [
            {"text": "Query planner/optimizer", "is_correct": True},
            {"text": "Auto-vacuum", "is_correct": False},
            {"text": "WAL (Write-Ahead Logging)", "is_correct": False},
            {"text": "Connection pooling", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of VACUUM in PostgreSQL?",
        "explanation": "VACUUM reclaims storage occupied by dead tuples and updates statistics used by the query planner. It's essential for maintaining database performance and preventing transaction ID wraparound.",
        "reference": "https://www.postgresql.org/docs/current/sql-vacuum.html",
        "points": 1,
        "answers": [
            {"text": "Reclaim storage and update statistics", "is_correct": True},
            {"text": "Create database backups", "is_correct": False},
            {"text": "Compress database files", "is_correct": False},
            {"text": "Validate data integrity", "is_correct": False}
        ]
    }
]
