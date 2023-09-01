from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId

from app.models.arsenal import models

MONGODB_DAAS_URI = "mongodb+srv://nikhilmiranda:vtTtF9mipllnscl3@purple-parrot.slcsytn.mongodb.net/"

# creating a client
mongo_client = MongoClient(MONGODB_DAAS_URI)


def connection(database: str, collection: str):
    return mongo_client[database][collection]
