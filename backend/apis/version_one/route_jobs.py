from database.repository.jobs import create_new_job_post
from database.repository.jobs import get_job_post_from_id
from database.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.jobs import JobCreate
from schemas.jobs import ShowJob
from sqlalchemy.orm import Session

# i need to create a job schema


# do i need to do a get request to get the owner_id?

job_router = APIRouter()


@job_router.post("/create-job/", response_model=ShowJob)
# JobCreate is there to validate the typing of each fields in job_post
def create_job_post(job_post: JobCreate, db: Session = Depends(get_db)):
    # assume id 1 for current_user
    current_user = 1
    job = create_new_job_post(job=job_post, db=db, owner_id=current_user)
    return job


@job_router.get("/get-jobs/{job_id}", response_model=ShowJob)
def retreive_job_posts(job_id: int, db: Session = Depends(get_db)):
    job = get_job_post_from_id(id=job_id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {job_id} does not exist",
        )
    return job
