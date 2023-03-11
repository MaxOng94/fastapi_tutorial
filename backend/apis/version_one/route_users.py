from database.repository.users import create_new_user
from database.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.users import ShowUser
from schemas.users import UserCreate
from sqlalchemy.orm import Session


router = APIRouter()


# the inputs to the create_user() function are from request
# UserCreate schema will do the validation of having a userename,
# email, password
# adding response_model =ShowUser to limit the number of fields back to user
@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
