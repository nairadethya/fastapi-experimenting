from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get("/")
async def home():
    data = {
        "text":"hi"
    }
    return {"data":data}

@app.get("/page/{page_name}")
async def page(page_name: str):

    data = {
        "page":page_name
    }

    return {"data":data}