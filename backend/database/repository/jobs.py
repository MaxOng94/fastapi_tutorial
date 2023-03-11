# this is where we interact with the database.
from database.models.base import Jobs
from schemas.jobs import JobCreate
from sqlalchemy.orm import Session


def create_new_job_post(job: JobCreate, db: Session, owner_id: int):
    job = Jobs(
        title=job.title,
        company=job.company,
        company_url=job.company_url,
        location=job.location,
        description=job.description,
        date_posted=job.date_posted,
        is_active=True,
        owner_id=owner_id,
    )

    db.add(job)
    db.commit()
    # refresh the job instance
    db.refresh(job)
    return job


# get job post based on job_id


def get_job_post_from_id(id: int, db: Session):
    return db.query(Jobs).filter(Jobs.id == id).first()
