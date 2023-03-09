from fastapi import APIRouter

from apis.version_one import route_general_pages
from apis.version_one import route_users
from apis.version_one import route_jobs


api_router = APIRouter()

api_router.include_router(route_general_pages.general_pages_router,prefix = "",tags= ["general_pages"])
api_router.include_router(route_users.router,prefix = '/users',tags = ['users'])
api_router.include_router(route_jobs.job_router,prefix = '/jobs',tags = ["jobs"])


