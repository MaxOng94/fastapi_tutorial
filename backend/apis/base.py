from apis.version_one import route_general_pages
from apis.version_one import route_jobs
from apis.version_one import route_users
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(
    route_general_pages.general_pages_router, prefix="", tags=["general_pages"]
)
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
# i am prefixing all the routes under the job_router with /jobs, 
# APIRoute(path='/jobs/create-job/', name='create_job_post', methods=['POST']), APIRoute(path='/jobs/get-jobs/{job_id}', name='retreive_job_posts', methods=['GET']), APIRoute(path='/jobs/all-jobs/', name='read_jobs', methods=['GET'])
api_router.include_router(route_jobs.job_router, prefix="/jobs", tags=["jobs"])
print(api_router.routes)

