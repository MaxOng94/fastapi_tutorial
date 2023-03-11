from datetime import date
from datetime import datetime
from typing import Union

from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    company_url: str
    location: str
    description: str
    date_posted: Union[date, None] = datetime.now().date()
    owner_id: int
    # i think we can automatically create date_posted
    # do we need owner_id and owner?


class ShowJob(BaseModel):
    id: int
    title: str
    company: str
    company_url: Union[str, None]
    location: str
    description: Union[str, None]
    date_posted: date
    is_active: bool

    # only when we declare orm_mode = True, sqlalchemy will go and extract the
    # relationship data, which is the owner_id
    class Config:
        orm_mode = True
