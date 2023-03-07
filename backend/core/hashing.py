from passlib.context import CryptContext
from typing import Boolean 


pwd_context = CryptContext(schemes=['bcrypt'],deprecated = "auto")


class Hasher():
    # staticmethod can be called by the class itself, do not need to 
    # create a class instance/object 
    @staticmethod
    def verify_password(plain_password:str, hashed_password:str) ->Boolean(): 
        return pwd_context.verify(plain_password,hashed_password)
    
    #Author felt that there was no need to be called by class instance/object
    @staticmethod
    def get_password_hash(password:str) -> str:
        return pwd_context.hash(password)
    


