import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONNECTION = str(os.getenv("DB_CONNECTION"))
engine = create_engine(
    DB_CONNECTION, pool_size=30, max_overflow=10
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@DeprecationWarning
def get_db():
    print("*** | THE FOLLOWING FUNCTION HAS BEEN DEPRECATED ON 5th SEPTEMBER 2022 | ***")
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
