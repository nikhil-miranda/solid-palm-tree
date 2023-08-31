from fastapi import APIRouter

# Adding api endpoint prefix for all routes in this file
router = APIRouter(prefix="/arsenal")


@router.get("/website-contact-message")
def get_website_contact_message():
    return {"message": "Success"}


@router.post("/website-contact-message")
def get_website_contact_message():


    return {"message": "Success"}
