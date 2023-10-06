import os

from pymongo import MongoClient

MONGODB_DAAS_URI = os.getenv("MONGO_DB_CONNECTION")

# creating a client
mongo_client = MongoClient(MONGODB_DAAS_URI, ssl=True)


def connection(database: str, collection: str):
    return mongo_client[database][collection]
