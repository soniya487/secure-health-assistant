from fastapi import APIRouter, Form, UploadFile, File, Depends
from app.utils.load_data import patient_df
from app.utils.auth import get_current_user
from app.utils.crypto_utils import encrypt_bytes, sha256_bytes
import requests, tempfile, os

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

# Basic text question (uses simple matching from recommendations/history)
@router.post("/ask")
def ask(message: str = Form(...), user=Depends(get_current_user)):
    # simple rule-based reply
    msg = message.lower()
    if "diabetes" in msg:
        return {"reply":"Common symptoms of diabetes: increased thirst, frequent urination, fatigue."}
    if "fever" in msg:
        return {"reply":"If fever > 38C for more than 48 hours see a doctor."}
    return {"reply":"I can help with symptoms, vitals, or prescriptions — tell me more."}

# Upload a document (encrypt + hash + store on chain)
@router.post("/upload/doc")
def upload_doc(file: UploadFile = File(...), user=Depends(get_current_user)):
    content = file.file.read()
    enc = encrypt_bytes(content)
    h = sha256_bytes(enc)
    # call blockchain store (proxy)
    cb_url = os.environ.get("BLOCKCHAIN_URL","http://127.0.0.1:8000/blockchain/store")
    try:
        r = requests.post(cb_url, json={"record_hash": h})
        chain_resp = r.json()
    except Exception as e:
        chain_resp = {"error":str(e)}
    return {"hash": h, "chain": chain_resp}
