from fastapi import APIRouter, UploadFile, File
from api.utils.file_parser import parse_file

router = APIRouter()

@router.post("/")
async def upload_cv(file: UploadFile = File(...)):
    content = await file.read()
    text = parse_file(file.filename, content)
    return {"text": text}
