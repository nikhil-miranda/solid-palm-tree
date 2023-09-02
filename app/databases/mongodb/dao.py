from datetime import datetime

from app.core.constants import *
from app.databases.mongodb.connect import connection
from app.models.arsenal import models


def read_all_messages(page_number: int = 1, page_size: int = 10):
    db = connection(database=MONGO_PORTFOLIO_WEBSITE_DB, collection=MONGO_MESSAGES_COLLECTION)
    messages = db.find().sort("_id", -1).skip((page_number - 1) * page_size).limit(page_size)
    return [models.Message(**message) for message in messages]


def create_message(payload: models.Message):
    # add current timestamp to payload
    payload.created_at = datetime.now().strftime("%d %B, %Y - %H:%M:%S")

    db = connection(database=MONGO_PORTFOLIO_WEBSITE_DB, collection=MONGO_MESSAGES_COLLECTION)
    message_id = db.insert_one(payload.model_dump()).inserted_id
    return {**payload.model_dump(), "id": str(message_id)}
