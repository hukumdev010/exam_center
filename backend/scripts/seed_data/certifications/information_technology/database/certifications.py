"""Database Certifications Data"""

from .mysql_database_administrator import CERTIFICATION as MYSQL_DBA_CERT
from .postgresql_database_administrator import (
    CERTIFICATION as POSTGRES_DBA_CERT
)
from .oracle_database_administration import CERTIFICATION as ORACLE_DBA_CERT
from .microsoft_sql_server_dba import CERTIFICATION as SQL_SERVER_DBA_CERT
from .mongodb_database_administrator import (
    CERTIFICATION as MONGODB_DBA_CERT
)
from .redis_database_administrator import CERTIFICATION as REDIS_DBA_CERT
from .cassandra_database_administrator import (
    CERTIFICATION as CASSANDRA_DBA_CERT
)
from .elasticsearch_database_administrator import (
     CERTIFICATION as ELASTICSEARCH_DBA_CERT
)

CERTIFICATIONS = [
    MYSQL_DBA_CERT,
    POSTGRES_DBA_CERT,
    ORACLE_DBA_CERT,
    SQL_SERVER_DBA_CERT,
    MONGODB_DBA_CERT,
    REDIS_DBA_CERT,
    CASSANDRA_DBA_CERT,
    ELASTICSEARCH_DBA_CERT
]