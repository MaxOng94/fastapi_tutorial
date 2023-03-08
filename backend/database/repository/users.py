# trying to follow a design pattern called repository
# the code that mainly interacts with the database 
# adding data, commiting etc are all separate from the route itself
# this makes it easier as the ORM code is separate from the route, in case we want to change ORMs

from sqlalchemy.orm import Session 

from schemas.users import UserCreate
from database.models.base import User
from core.hashing import Hasher

# this is where we really create a user and update it in our database 
# again user is from request, not sure how it will be captured and passed 
# usercreate is from pydantic, to validate the data that is coming through
def create_new_user(user:UserCreate,db:Session):
    user= User(username = user.username,
         email = user.email,
         hashed_password = Hasher.get_password_hash(user.password),
         is_active = True,
         is_superuser = False
         )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user 