import os

import asyncpg

DATABASE_URL = os.getenv("POSTGRESQL_DB_CONNECTION")


def connect():
    return asyncpg.connect(DATABASE_URL)
