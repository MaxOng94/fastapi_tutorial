from fastapi import APIRouter

from apis.version_one import route_general_pages
from apis.version_one import route_users


api_router = APIRouter()

api_router.include_router(route_general_pages.general_pages_router,prefix = "",tags= ["general_pages"])
api_router.include_router(route_users.router,prefix = '/users',tags = ['users'])

print(dir(api_router))
print(api_router.routes)