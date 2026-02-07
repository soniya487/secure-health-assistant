# minimal rule-based NER placeholder; replace with BioBERT finetuned model later
def extract_entities(text: str):
    out = []
    meds = ["aspirin","metformin","insulin"]
    conds = ["diabetes","hypertension","asthma","fever","cough","heart attack"]
    words = text.lower().split()
    for m in meds:
        if m in text.lower():
            out.append({"type":"MEDICATION","text":m})
    for c in conds:
        if c in text.lower():
            out.append({"type":"CONDITION","text":c})
    return out
