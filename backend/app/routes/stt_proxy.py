from fastapi import APIRouter, UploadFile, File
from app.services.stt_service import transcribe_audio

router = APIRouter(prefix="/stt", tags=["STT"])

@router.post("/transcribe")
def transcribe(file: UploadFile = File(...)):
    content = file.file.read()
    return transcribe_audio(content)
