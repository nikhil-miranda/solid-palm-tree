from app.core.constants import *
from app.models.arsenal import models
from app.databases.mongodb.connect import connection


def create_message(payload: models.Message):
    db = connection(database=MONGO_PORTFOLIO_WEBSITE_DB, collection=MONGO_MESSAGES_COLLECTION)
    message_id = db.insert_one(payload.model_dump()).inserted_id
    return {**payload.model_dump(), "id": str(message_id)}
