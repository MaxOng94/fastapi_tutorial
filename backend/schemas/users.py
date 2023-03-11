from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# adding this class to route_users.py @router decorator under response_model
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    # tells pydantic to convert even non dict obj to json
    class Config:
        orm_mode = True
