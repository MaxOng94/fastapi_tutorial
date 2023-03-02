#=================================
# standard imports 
from sqlalchemy import create_engine,ForeignKey,Column,String, Integer,CHAR
# declarative is the base class that every sub class is doing to inherit from
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
#=================================
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/pizza_db"

engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try: 
        yield db
    except: 
        db.close()

class Settings:
        PROJECT_NAME:str= "Job Board"
        PROJECT_VERSION:str = "1.0.0"
        
settings =Settings()