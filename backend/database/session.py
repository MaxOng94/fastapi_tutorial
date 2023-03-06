#==============================
# standard imports for sqlalchemy
from sqlalchemy import create_engine
from core.config import settings
#==============================

database_connection_string = settings.DB_CONNECTION_STRING
# sqlalchemy has a new version 2.0 
# future=True is to tell sqlalchemy to create the new style engine 
engine= create_engine(database_connection_string,future=True,echo=True)

sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

print(engine.dialect)