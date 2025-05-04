from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from utils.llama_interface import call_llama
from utils.pdf_parser import parse_pdf_or_docx
from utils.pdf_generator import generate_pdf_from_json
import tempfile

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.post("/upload")
async def upload_cv(file: UploadFile = File(...)):
    text = await parse_pdf_or_docx(file)
    return {"text": text}

@app.post("/customize")
async def customize_cv(data: dict):
    cv_text = data["cv_text"]
    job_role = data["job_role"]
    job_desc = data["job_desc"]
    return call_llama(cv_text, job_role, job_desc)

@app.post("/generate")
async def generate(json_data: dict):
    pdf_path = generate_pdf_from_json(json_data)
    return FileResponse(pdf_path, media_type="application/pdf", filename="customized_cv.pdf")
