from sqlalchemy.orm import Session

from app.databases.sqlite import schemas


def fetch_profile_view_counter_by_github_username(db: Session, github_username: str):
    return db.query(schemas.GithubProfileViewCounter).filter(
        schemas.GithubProfileViewCounter.github_username == github_username).one_or_none()


def upsert_profile_view_counter_by_github_username(db: Session, github_username: str):
    profile_view_counter = schemas.GithubProfileViewCounter(github_username=github_username, counter=1)

    existing_counter = fetch_profile_view_counter_by_github_username(db=db, github_username=github_username)

    if existing_counter is not None:
        profile_view_counter.counter = existing_counter.counter + 1

    db.merge(profile_view_counter)
    db.commit()

    return profile_view_counter.counter
