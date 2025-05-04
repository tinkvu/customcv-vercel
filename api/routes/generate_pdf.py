from fastapi import APIRouter, Body
from fastapi.responses import FileResponse
from api.utils.json_to_pdf import generate_pdf_from_json
import uuid

router = APIRouter()

@router.post("/")
def generate_pdf(cv_json: dict = Body(...)):
    filename = f"/tmp/{uuid.uuid4().hex}.pdf"
    generate_pdf_from_json(cv_json, filename)
    return FileResponse(filename, media_type='application/pdf', filename="customized_cv.pdf")
