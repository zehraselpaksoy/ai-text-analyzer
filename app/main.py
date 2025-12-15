from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app import services, logger

app = FastAPI(title="AI Text Analyzer")

# templates klasörünün yolu
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    logger.log("Root endpoint called")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze_form", response_class=HTMLResponse)
async def analyze_form(request: Request, text: str = Form(...)):
    logger.log("Analyze (form) endpoint called")
    result = services.analyze_text(text)
    return templates.TemplateResponse("result.html", {"request": request, "result": result})
