from sqlalchemy import Column, Integer, String

from app.databases.sqlite.connect import Base


class GithubProfileViewCounter(Base):
    __tablename__ = 'github_profile_view_counter'

    github_username = Column(String, primary_key=True)
    counter = Column(Integer, nullable=False)
    ip_address = Column(String, nullable=True)
    region = Column(String, nullable=True)
