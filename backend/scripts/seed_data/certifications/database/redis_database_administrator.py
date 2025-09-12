"""Redis Database Administrator Certification"""

CERTIFICATION = {
    "name": "Redis Database Administrator",
    "description": "Redis in-memory data structure store administration, clustering, and optimization",
    "slug": "redis-database-administrator",
    "level": "Intermediate",
    "duration": 90,
    "questions_count": 50,
    "category_slug": "database",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What type of database is Redis?",
        "explanation": "Redis is an in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures like strings, hashes, lists, sets, and sorted sets.",
        "reference": "https://redis.io/documentation",
        "points": 1,
        "answers": [
            {"text": "In-memory data structure store", "is_correct": True},
            {"text": "Relational database", "is_correct": False},
            {"text": "Document database", "is_correct": False},
            {"text": "Graph database", "is_correct": False}
        ]
    },
    {
        "text": "Which Redis data type would you use for a leaderboard?",
        "explanation": "Sorted Sets (ZSET) are ideal for leaderboards because they maintain elements in sorted order by score, allowing for efficient range queries and ranking operations.",
        "reference": "https://redis.io/docs/data-types/sorted-sets/",
        "points": 1,
        "answers": [
            {"text": "Sorted Set (ZSET)", "is_correct": True},
            {"text": "List", "is_correct": False},
            {"text": "Hash", "is_correct": False},
            {"text": "String", "is_correct": False}
        ]
    },
    {
        "text": "What is Redis persistence?",
        "explanation": "Redis persistence allows data to survive server restarts by writing data to disk. Redis offers RDB snapshots and AOF (Append Only File) logging for different persistence needs.",
        "reference": "https://redis.io/docs/manual/persistence/",
        "points": 1,
        "answers": [
            {"text": "Writing data to disk to survive restarts", "is_correct": True},
            {"text": "Keeping data only in memory", "is_correct": False},
            {"text": "Replicating data to other servers", "is_correct": False},
            {"text": "Compressing data structures", "is_correct": False}
        ]
    },
    {
        "text": "What is Redis Cluster?",
        "explanation": "Redis Cluster provides automatic sharding across multiple Redis nodes, offering high availability and horizontal scaling by distributing data across multiple masters.",
        "reference": "https://redis.io/docs/manual/scaling/",
        "points": 1,
        "answers": [
            {"text": "Automatic sharding across multiple Redis nodes", "is_correct": True},
            {"text": "A single Redis instance with multiple databases", "is_correct": False},
            {"text": "A backup and recovery solution", "is_correct": False},
            {"text": "A monitoring tool for Redis", "is_correct": False}
        ]
    },
    {
        "text": "Which Redis command is used to set a key expiration time?",
        "explanation": "EXPIRE sets a timeout on a key, after which the key will automatically be deleted. TTL can be used to check the remaining time to live of a key.",
        "reference": "https://redis.io/commands/expire/",
        "points": 1,
        "answers": [
            {"text": "EXPIRE", "is_correct": True},
            {"text": "TIMEOUT", "is_correct": False},
            {"text": "DELETE", "is_correct": False},
            {"text": "REMOVE", "is_correct": False}
        ]
    }
]
