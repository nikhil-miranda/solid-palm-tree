from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.databases.sqlite import get_db
from app.services.github import services

router = APIRouter(prefix="/github")


@router.post("/profile-view-counter/{github_username}")
def record_profile_view(github_username: str, db: Session = Depends(get_db)):
    return services.record_profile_view_count(db=db, github_username=github_username)
