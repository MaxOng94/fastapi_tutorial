from sqlalchemy.orm import sessionmaker,declarative_base, as_declarative,declared_attr 


@as_declarative()
class Base(object):
    @declared_attr
    # __tablename__ is a class level method
    def __tablename__(cls):
        return cls.__name__.lower()