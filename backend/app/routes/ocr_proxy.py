from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import ocr_image

router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/read")
def read(file: UploadFile = File(...)):
    content = file.file.read()
    return ocr_image(content)
