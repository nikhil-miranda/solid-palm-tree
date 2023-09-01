from traceback import print_exc

from app.databases.mongodb import dao
from app.models.arsenal import models


def store_message(payload: models.Message):
    try:
        return dao.create_message(payload=payload)
    except Exception as e:
        print_exc()
        return {"error": "Failed to store message.", "e": str(e)}
