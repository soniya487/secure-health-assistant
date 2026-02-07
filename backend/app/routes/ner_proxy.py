from fastapi import APIRouter, Body
from app.services.ner_service import extract_entities

router = APIRouter(prefix="/ner", tags=["NER"])

@router.post("/extract")
def extract(payload: dict = Body(...)):
    text = payload.get("text","")
    ents = extract_entities(text)
    return {"entities": ents}
