from fastapi import FastAPI
from backend.auth_routes import auth_router
from backend.order_routes import order_router
from pydantic import BaseModel 

app = FastAPI()


app.include_router(auth_router)
app.include_router(order_router)


# in fastapi, the order of the path is important as path are evaluated in order

@app.get("/")
async def root():
    return {"message":"Hello world"}

# @app.post("/auth/signup")