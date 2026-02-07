from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/imaging", tags=["Imaging"])

try:
    from app.services.imaging_service import infer_image
    IMAGING_ENABLED = True
except Exception:
    infer_image = None
    IMAGING_ENABLED = False


@router.post("/analyze")
def analyze(file: UploadFile = File(...)):
    if not IMAGING_ENABLED:
        raise HTTPException(
            status_code=503,
            detail="Imaging service is disabled because torch/torchvision are not installed."
        )

    content = file.file.read()
    result = infer_image(content)
    return result
