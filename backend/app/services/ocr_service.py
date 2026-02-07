from PIL import Image
import pytesseract, io

def ocr_image(image_bytes: bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(img)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
