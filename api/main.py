from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import upload, customize, generate_pdf
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload")
app.include_router(customize.router, prefix="/customize")
app.include_router(generate_pdf.router, prefix="/generate")
