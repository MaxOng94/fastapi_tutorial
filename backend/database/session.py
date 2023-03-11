# ==============================
# standard imports for sqlalchemy
import pathlib
import sys
from typing import Generator

# sqlalchemy core provides connection to database, 
# interacting with sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

backend_directory = (pathlib.Path(__file__) / ".." / "..").resolve()

sys.path.append(str(backend_directory))
from core.config import settings

# ==============================

database_connection_string = settings.DB_CONNECTION_STRING
# sqlalchemy has a new version 2.0
# future=True is to tell sqlalchemy to create the new style engine
engine = create_engine(database_connection_string, future=True, echo=True)

# sessionmaker is to create a factory for session object, which interacts with the database within this 'period'
# session as a way to interact with database in sqlalchemy
# autocommit: sends a commit statement that tells the database our transaction is final and should persist
# flush : is to execute the sql; to update the database
# sessionlocal as our session object
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# because of the yield keyword


def get_db() -> Generator:
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()
