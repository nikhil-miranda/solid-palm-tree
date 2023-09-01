from fastapi import APIRouter

from app.models.arsenal import models
from app.services.arsenal import services

# Adding api endpoint prefix for all routes in this file
router = APIRouter(prefix="/arsenal")


@router.get("/website-contact-message")
def get_website_contact_message():
    return {"message": "Success"}


@router.post("/website-contact-message")
def post_website_contact_message(request_payload: models.Message):
    return services.store_message(payload=request_payload)
