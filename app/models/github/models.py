from typing import Optional

from pydantic import BaseModel, Field


class GithubProfileViewCounter(BaseModel):
    github_username: str = Field(..., example='johndoe')
    counter: int = Field(..., example=0)
    ip_address: Optional[str] = Field(None, example='192.121.124.39')
    region: Optional[str] = Field(None, example='India')
