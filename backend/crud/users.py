# trying to follow a design pattern called repository
# the code that mainly interacts with the database
# adding data, commiting etc are all separate from the route itself
# this makes it easier as the ORM code is separate from the route, in case we want to change ORMs
from core.hashing import Hasher
from database.models.base import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session

# this is where we really create a user and update it in our database
# again user is from request, not sure how it will be captured and passed
# usercreate is from pydantic, to validate the data that is coming through


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )

    db.add(user)
    db.commit()
    # refresh the user instance, so the user is updated with the most-up to date data from the database
    # this is important so our response body contains updated information when showing user
    db.refresh(user)
    return user


def get_username_from_user_id(id: int, db: Session):
    username = db.query(User.username).filter(User.id == id).first()
    # first method return the result as a tuple (result), 
    # or None if no rows are returned
    if username:
        return username[0]
    else: 
        return None 