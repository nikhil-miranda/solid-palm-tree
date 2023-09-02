from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    name: str
    email: str
    message: str
    created_at: Optional[str] = None
