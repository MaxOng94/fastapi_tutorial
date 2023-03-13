# this is where we interact with the database.
from database.models.base import Jobs
from schemas.jobs import JobCreate
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

# documentation for session's query API
# https://docs.sqlalchemy.org/en/14/orm/query.html

def create_new_job_post(job: JobCreate, db: Session):
    job = Jobs(
        title=job.title,
        company=job.company,
        company_url=job.company_url,
        location=job.location,
        description=job.description,
        date_posted=job.date_posted,
        is_active=True,
        owner_id=job.owner_id,
    )

    db.add(job)
    db.commit()
    # refresh the job instance
    db.refresh(job)
    return job


# get job post based on job_id


def get_job_post_from_id(id: int, db: Session):
    return db.query(Jobs).filter(Jobs.id == id).first()


def get_all_job_posts(db:Session):
    jobs = db.query(Jobs).filter(Jobs.is_active==True).all()
    # will return the results in a list 
    return jobs

# put request is to update 
# should be already at the id endpoint to update.
def update_job_by_id(job: JobCreate,id:int, db:Session):
    # 1) first check if job id is already in db, if not just add
    # 2) Show a message that tells them no job found, do you want to add? 
    # first chec
    # sess.query(User).filter(User.age == 25).\
    # update({User.age: User.age - 10}, synchronize_session=False)
    existing_job = db.query(Jobs).filter(Jobs.id ==id).first()
    for key,value in job.dict().items():
        # updating each attribute in our existing_job with the newly provided job
        setattr(existing_job,key,value)
        
        # setattr is a built-in Python function that allows you to set the value of an attribute of an object. 
        # The function takes three arguments: the object, the name of the attribute as a string, and the value to set the attribute to.
        # For example, if you have an object x with an attribute a, you can set the value of a to 5 using setattr like this:
        # x = MyClass()
        # setattr(x, 'a', 5)

    db.commit()
    return existing_job


def get_all_jobs_from_user_id(owner_id : int, db:Session):
    jobs = db.query(Jobs).filter(Jobs.owner_id== owner_id).all()
    return jobs 


def delete_job_from_id(id:int,db:Session):
    job = db.query(Jobs).filter(Jobs.id == id).first()
    if job: 
        db.delete(job)
        db.commit()
        return job
    else: 
        return None