from fastapi import FastAPI
# 
from fastapi.staticfiles import StaticFiles
from apis.general_pages.route_homepage import general_pages_router 
from core.config import settings
from pydantic import BaseModel 
from database.base_class import Base
from database.session import engine

# The first "/static" refers to the sub-path this "sub-application" will be "mounted" on. So, any path that starts with "/static" will be handled by it.
# The directory="static" refers to the name of the directory that contains your static files.
# The name="static" gives it a name that can be used internally by FastAPI.
# All these parameters can be different than "static", adjust them with the needs and specific details of your own application.


def start_application():
    app=FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(general_pages_router)
    app.mount("/static",StaticFiles(directory="static"),name= "static")
    Base.metadata.create_all(bind=engine)
    return app
# in fastapi, the order of the path is important as path are evaluated in order

app = start_application()