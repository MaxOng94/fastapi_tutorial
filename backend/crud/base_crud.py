# to create a base CRUD class to be inherited by other sub classes 
from typing import TypeVar
from pydantic import BaseModel 
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
# jsonable_encoder is able to convert data types (like pydantic model) to something that is 
# compatible with json (dictionary or list etc)




"""
T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
"""
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase():
    def __init__():
        """
        CRUD object supplying default methods to 
        Create
        Read
        Update
        Delete
        """


        pass 

    def create():
        pass 

    def update():

        # isinstance checks if an object is an instance of a class
        # or a subclass of other class, and returns True and False if otherwise 
        pass 

    def get():
        pass

    def remove():
        pass
