#================
'''
conftest.py is a special file in pytest, where we can store our fixtures here to be shared across 
multiple test modules. 
Any fixture or confituation in conftest.py is automatically discovered by pytest
'''
#===============

from typing import Any, Generator 

import pytest 

from fastapi import FastAPI
# testclient can help us test FastAPI application 
# by simulating http requests and responses  
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
# sessionmaker as a factory to create session objs
# where we interact with dbs within these session objs 
from sqlalchemy.orm import sessionmaker 

import sys 
import pathlib 

# resolves make it an absolute path 
backend_directory= (pathlib.Path(__file__)/".."/"..").resolve()
# append the directory to sys.path, 
# this adds the backend_directory to python module search path, so we can import modules from backend directory
# however, sys.path.append takes in string, so we add str in front
sys.path.append(str(backend_directory))

from database.base_class import Base
from database.session import get_db
from apis.base import api_router

def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app 

# print(api_router.routes)

# create a test sqlalchemy_connection_str so all our test data goes into this test db
# will not contaminate our production db 
TESTING_SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"

engine = create_engine(TESTING_SQLALCHEMY_DATABASE_URL,
                       connect_args = {"check_same_thread":False})

# create a SessionTesting  to interact with our test database 
SessionTesting =sessionmaker(autocommit=False,autoflush=False, bind = engine)


# Fixtures are defined using the @pytest.fixture decorator, which marks a module as a fixture. The decorator can take an optional scope argument, which determines how often the fixture is invoked. The available scope options are:

# function: The fixture is invoked once per test function (the default).
# class: The fixture is invoked once per test class.
# module: The fixture is invoked once per test module.
# session: The fixture is invoked once per test session.

@pytest.fixture(scope="module")
def app() -> Generator[FastAPI,Any,None]:
    """
    Will create a fresh database on each test case 
    By using a generator function as our fixuture, we can use the 
    yield keyword to pause the function execution after creating the application instance and 
    running the test case, but before dropping our database tables. 
    This allows us to inspect the state of the database after running test cases, if necessary. 
    """
    Base.metadata.create_all(engine) # create all the tables 
    _app = start_application()
    yield _app 
    Base.metadata.drop_all(engine)


@pytest.fixture(scope = "module")
def db_session(app: FastAPI) -> Generator[SessionTesting ,Any,None]:
    connection = engine.connect()
    transaction =connection.begin()
    session = SessionTesting (bind=connection)
    yield session # use the session in tests 
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="module")
def client(
    app: FastAPI, db_session: SessionTesting 
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
