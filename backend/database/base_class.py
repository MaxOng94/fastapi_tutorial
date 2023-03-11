from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class Base(object):
    @declared_attr
    # __tablename__ is a class level method
    def __tablename__(cls):
        return cls.__name__.lower()
