from sqlalchemy.orm import Session

from app.databases.sqlite import dao


def record_profile_view_count(db: Session, github_username: str):
    return dao.upsert_profile_view_counter_by_github_username(db=db, github_username=github_username)
