from fastapi import APIRouter

from app.models.arsenal import models
from app.services.arsenal import services

# Adding api endpoint prefix for all routes in this file
router = APIRouter(prefix="/arsenal")


@router.get("/website-contact-message")
def fetch_website_contact_messages(page_number: int = 1, page_size: int = 10):
    return services.fetch_messages(page_number=page_number, page_size=page_size)


@router.post("/website-contact-message")
def store_website_contact_message(request_payload: models.Message):
    return services.store_message(payload=request_payload)
