from apis.version_one import route_general_pages
from apis.version_one import route_jobs
from apis.version_one import route_users
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(
    route_general_pages.general_pages_router, prefix="", tags=["general_pages"]
)
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.job_router, prefix="/jobs", tags=["jobs"])

# api_router.include_router(route_jobs.job_router,prefix = '/create-jobs',tags = ["jobs"])
# api_router.include_router(route_jobs.job_router,prefix = '/get-jobs/1',tags = ["get-jobs"])

print(api_router.routes)
