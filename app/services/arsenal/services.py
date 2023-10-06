from traceback import print_exc

from app.databases.mongodb import dao
from app.models.arsenal import models


def fetch_messages(page_number: int = 1, page_size: int = 10):
    try:
        return dao.read_all_messages(page_number=page_number, page_size=page_size)
    except Exception as e:
        print_exc()
        return {"error": "Failed to fetch messages.", "e": str(e)}


def store_message(payload: models.Message):
    if payload.name is None and payload.email is None and payload.message is None:
        return {"message": "Details were sent empty."}

    if payload.name is "string" and payload.email is "string" and payload.message is "string":
        return {"message": "Details were sent empty."}

    try:
        return dao.create_message(payload=payload)
    except Exception as e:
        print_exc()
        return {"error": "Failed to store message.", "e": str(e)}
