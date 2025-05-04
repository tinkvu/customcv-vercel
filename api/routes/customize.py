from fastapi import APIRouter, Body
from api.utils.llama_interface import call_llama

router = APIRouter()

@router.post("/")
async def customize_cv(cv_text: str = Body(...), job_role: str = Body(...), job_desc: str = Body(...)):
    return call_llama(cv_text, job_role, job_desc)
