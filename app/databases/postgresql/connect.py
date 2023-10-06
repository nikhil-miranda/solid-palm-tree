import psycopg2
import asyncpg

DATABASE_URL = "postgres://nikhil.miranda:e03aYFQOgAwd@ep-sweet-wind-20949678.ap-southeast-1.aws.neon.tech/neondb"


def connect():
    return asyncpg.connect(DATABASE_URL)


