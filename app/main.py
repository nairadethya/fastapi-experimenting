from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page":"Home page"
    }
    return templates.TemplateResponse("page.html", {"request":request, "data": data})

@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):

    data = {
        "page":page_name
    }

    return templates.TemplateResponse("page.html", {"request":request, "data": data})