import os
from app.routes.auth import router as auth_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import patient, vitals, chatbot, ner_proxy, imaging_proxy, stt_proxy, ocr_proxy, blockchain_proxy
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"), override=True)

app = FastAPI(title="Secure Multimodal Healthcare Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(auth_router)
app.include_router(patient.router)
app.include_router(vitals.router)
app.include_router(chatbot.router)
app.include_router(ner_proxy.router)
app.include_router(imaging_proxy.router)
app.include_router(stt_proxy.router)
app.include_router(ocr_proxy.router)
app.include_router(blockchain_proxy.router)

@app.get("/")
def root():
    return {"message":"Secure Multimodal Healthcare Chatbot API running"}
from fastapi.responses import Response

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)
