from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": ""}
    )

@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    # Simple demo validation
    if username == "admin" and password == "password":
        message = "Login successful!"
    else:
        message = "Invalid username or password"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": message}
    )
