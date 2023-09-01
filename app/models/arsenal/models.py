from pydantic import BaseModel


class Message(BaseModel):
    name: str
    email: str
    message: str
