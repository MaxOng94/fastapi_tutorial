from fastapi import APIRouter 

# each router will be an instance of the APIRouter class
# routers, different routes for different funtionalities we might have

order_router= APIRouter()


@order_router.get('/')
async def hello():
    return {"message":"Hello world"}