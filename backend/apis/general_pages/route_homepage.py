from fastapi import FastAPI 
from fastapi import APIRouter 
from fastapi import Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# we tell jinja that ithas to look for html under the templates folder 
templates = Jinja2Templates(directory="templates")

# use the api router to keep code clean
general_pages_router = APIRouter()


@general_pages_router.get('/')
# what can the home function take in and what can it not take in? 
async def home(request:Request):
    return templates.TemplateResponse("general_pages/homepage.html",{"request":request})

