from database.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


# jobs
class Jobs(Base):
    # do not need to declare table name, as the Base class is written using the @declared_attr
    # that names the table using its class name
    # create index for the id column, if we search the table use the id
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(String)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # "User" is the name of the table
    # use relationship + back_populate can help
    owner = relationship("User", back_populates="jobs")


# users
# who posted the job
class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    # back_populates column name
    jobs = relationship("Jobs", back_populates="owner")


print(User.__tablename__)
