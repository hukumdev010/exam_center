"""Cassandra Database Administrator Certification"""

CERTIFICATION = {
    "name": "Apache Cassandra Database Administrator",
    "description": "Cassandra NoSQL distributed database administration, clustering, and performance tuning",
    "slug": "cassandra-database-administrator",
    "level": "Advanced",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "database",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the CAP theorem and how does Cassandra handle it?",
        "explanation": "The CAP theorem states you can only guarantee 2 of 3: Consistency, Availability, and Partition tolerance. Cassandra chooses Availability and Partition tolerance, offering eventual consistency.",
        "reference": "https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html",
        "points": 1,
        "answers": [
            {
                "text": "Cassandra chooses Availability and Partition tolerance over Consistency",
                "is_correct": True,
            },
            {
                "text": "Cassandra chooses Consistency and Availability over Partition tolerance",
                "is_correct": False,
            },
            {
                "text": "Cassandra provides all three: Consistency, Availability, and Partition tolerance",
                "is_correct": False,
            },
            {"text": "Cassandra only provides Consistency", "is_correct": False},
        ],
    },
    {
        "text": "What is a partition key in Cassandra?",
        "explanation": "A partition key determines which node in the cluster stores a particular row. It's used to distribute data across the cluster and must be specified in queries to locate data efficiently.",
        "reference": "https://cassandra.apache.org/doc/latest/cassandra/cql/ddl.html#the-partition-key",
        "points": 1,
        "answers": [
            {
                "text": "A key that determines which node stores a row",
                "is_correct": True,
            },
            {"text": "A key that encrypts data", "is_correct": False},
            {"text": "A key that sorts data within a partition", "is_correct": False},
            {"text": "A key that creates database backups", "is_correct": False},
        ],
    },
    {
        "text": "What is eventual consistency in Cassandra?",
        "explanation": "Eventual consistency means that given enough time and no new updates, all replicas will converge to the same value. Cassandra uses this model to provide high availability and partition tolerance.",
        "reference": "https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html#eventual-consistency",
        "points": 1,
        "answers": [
            {
                "text": "All replicas will eventually have the same data",
                "is_correct": True,
            },
            {
                "text": "Data is immediately consistent across all nodes",
                "is_correct": False,
            },
            {"text": "Data is never consistent", "is_correct": False},
            {"text": "Only one node has consistent data", "is_correct": False},
        ],
    },
    {
        "text": "What is a keyspace in Cassandra?",
        "explanation": "A keyspace in Cassandra is similar to a database in relational systems. It contains tables and defines replication strategy and replication factor for the data within it.",
        "reference": "https://cassandra.apache.org/doc/latest/cassandra/cql/ddl.html#create-keyspace",
        "points": 1,
        "answers": [
            {
                "text": "A container for tables that defines replication strategy",
                "is_correct": True,
            },
            {"text": "A single row of data", "is_correct": False},
            {"text": "A backup file", "is_correct": False},
            {"text": "A query execution plan", "is_correct": False},
        ],
    },
    {
        "text": "What is compaction in Cassandra?",
        "explanation": "Compaction is the process of merging SSTables (Sorted String Tables) to improve read performance, reclaim disk space, and remove deleted data permanently.",
        "reference": "https://cassandra.apache.org/doc/latest/cassandra/operating/compaction/index.html",
        "points": 1,
        "answers": [
            {
                "text": "Merging SSTables to improve performance and reclaim space",
                "is_correct": True,
            },
            {"text": "Compressing data to save disk space", "is_correct": False},
            {"text": "Creating database indexes", "is_correct": False},
            {"text": "Backing up database files", "is_correct": False},
        ],
    },
]
