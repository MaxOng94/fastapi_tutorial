from fastapi import APIRouter 

# each router will be an instance of the APIRouter class

auth_router= APIRouter()


@auth_router.get('/')
async def hello():
    return {"message":"Hello world"}