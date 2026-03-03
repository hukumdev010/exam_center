"""Database Certifications Module"""

from . import (
    cassandra_database_administrator,
    elasticsearch_database_administrator,
    microsoft_sql_server_dba,
    mongodb_database_administrator,
    mysql_database_administrator,
    oracle_database_administration,
    postgresql_database_administrator,
    redis_database_administrator,
)

# Collect all Database certifications
CERTIFICATIONS = []
ALL_QUESTIONS = {}

# Import certifications and questions from all modules
modules = [
    oracle_database_administration,
    microsoft_sql_server_dba,
    mysql_database_administrator,
    postgresql_database_administrator,
    mongodb_database_administrator,
    redis_database_administrator,
    cassandra_database_administrator,
    elasticsearch_database_administrator,
]

for module in modules:
    CERTIFICATIONS.append(module.CERTIFICATION)
    if hasattr(module, "QUESTIONS") and module.QUESTIONS:
        ALL_QUESTIONS[module.CERTIFICATION["slug"]] = module.QUESTIONS

__all__ = ["CERTIFICATIONS", "ALL_QUESTIONS"]
