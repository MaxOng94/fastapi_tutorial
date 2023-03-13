from crud.jobs import create_new_job_post,get_all_job_posts,get_job_post_from_id,get_all_jobs_from_user_id,update_job_by_id
from crud.users import get_username_from_user_id
from database.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.jobs import JobCreate
from schemas.jobs import ShowJob
from sqlalchemy.orm import Session
from typing import List

# i need to create a job schema


# do i need to do a get request to get the owner_id?

job_router = APIRouter()


@job_router.post("/create-job/", response_model=ShowJob)
# JobCreate is there to validate the typing of each fields in job_post
def create_job_post(job_post: JobCreate, db: Session = Depends(get_db)) -> ShowJob:
    # assume id 1 for current_user
    # current_user = 1
    job = create_new_job_post(job=job_post, db=db)
    return job


@job_router.get("/get-jobs/{job_id}", response_model=ShowJob)
def retreive_job_posts(job_id: int, db: Session = Depends(get_db)) -> ShowJob:
    job = get_job_post_from_id(id=job_id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {job_id} does not exist",
        )
    return job

@job_router.get("/get-all-jobs/{user_id}", response_model=List[ShowJob])
def retreive_job_posts(user_id:int, db: Session = Depends(get_db)) -> List[ShowJob]:
    username= get_username_from_user_id(id = user_id, db = db)
    job = get_all_jobs_from_user_id(owner_id=user_id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hey {username}, from our record, you have not posted any jobs. Start posting some jobs today!",
        )
    return job


@job_router.put("/update/{job_id}",response_model=ShowJob)
def update_job_post(job: JobCreate,job_id:int, db : Session = Depends(get_db)) -> ShowJob:
    jobs = update_job_by_id(job =job, id=job_id,db=db)
    return jobs



# see the example of returning a list of pydantic object
# https://fastapi.tiangolo.com/tutorial/response-model/
@job_router.get("/all-jobs/",response_model=List[ShowJob])
def read_jobs(db : Session = Depends(get_db)) -> List[ShowJob]:
    jobs = get_all_job_posts(db=db)
    return jobs


