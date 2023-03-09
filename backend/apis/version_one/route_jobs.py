from fastapi import APIRouter, Depends
from schemas.jobs import JobCreate ,ShowJob
from sqlalchemy.orm import Session
from database.repository.jobs import create_new_job_post
from database.session import get_db
# i need to create a job schema


# do i need to do a get request to get the owner_id?

job_router = APIRouter()



@job_router.post('/',response_model = ShowJob)
# JobCreate is there to validate the typing of each fields in job_post
def create_job_post(job_post: JobCreate, db: Session = Depends(get_db)):
    # assume id 1 for current_user 
    current_user = 1
    job = create_new_job_post(job=job_post, db= db,owner_id=current_user)
    return job