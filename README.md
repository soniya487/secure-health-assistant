** Secure Multimodal Healthcare Assistant**
A FastAPI-based backend system that simulates a secure, multimodal healthcare assistant.

This project demonstrates how patient data, medical history, vitals, chatbot interaction, imaging, OCR, speech-to-text, and blockchain logging can be integrated into a single backend system for academic and demonstration purposes.

⚠️ Disclaimer:
This project is for educational/demo use only. It does not provide real medical diagnosis or treatment.

**Key Features**
**Authentication** (OAuth2 – Demo Mode)

**Patient Data Management**

**❤️ Health Vitals Monitoring**

**💬 Chatbot API (text-based interaction)**

**🧠 NER (Named Entity Recognition) Endpoint**

**🖼️ Medical Imaging Analysis (stub/demo)**

**📝 OCR (document reading – demo)**

**🎙️ Speech-to-Text API (demo)**

**⛓️ Blockchain Hash Storage (Solidity smart contract – demo)**

## Tech Stack

- **Backend:** FastAPI (Python)
- **Auth:** OAuth2 Password Flow (JWT – demo)
- **Data:** CSV files (pandas)
- **AI/ML (demo):** NER, imaging, OCR, STT
- **Blockchain:** Solidity smart contract (demo)
- **Docs:** Swagger UI (OpenAPI)

##  How to Run (Local)

```bash
# create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
# install dependencies
pip install -r requirements.txt

# run server
uvicorn app.main:app --reload

Open browser:
http://127.0.0.1:8000/docs

Demo Authentication

Token Endpoint

POST /token


Demo Credentials

username: soniya
password: 1234

Use Authorize button in Swagger UI to access protected endpoints.


📁 Project Structure
secure-health-assistant/
├── backend/
│   └── app/
│       ├── main.py                # FastAPI entry point
│       ├── routes/
│       │   ├── auth.py
│       │   ├── patient.py
│       │   ├── vitals.py
│       │   ├── chatbot.py
│       │   ├── imaging_proxy.py
│       │   ├── ocr_proxy.py
│       │   ├── stt_proxy.py
│       │   ├── ner_proxy.py
│       │   └── blockchain_proxy.py
│       └── utils/
│           └── load_data.py
├── data/
│   ├── patient_info.csv
│   ├── medical_history.csv
│   ├── health_vitals.csv
│   └── doctor_recommendations.csv
├── contracts/
│   └── SimpleStorage.sol
├── notebooks/
│   ├── fine_tune_biobert.ipynb
│   └── train_imaging.ipynb
├── requirements.txt
├── .gitignore
└── README.md


            
