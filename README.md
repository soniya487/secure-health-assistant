**Secure Multimodal Healthcare Assistant**

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

## How to Run Locally

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
2️⃣ Activate Environment

Windows (PowerShell)

.venv\Scripts\Activate.ps1


Windows (CMD)

.venv\Scripts\activate.bat


macOS / Linux

source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Server
uvicorn app.main:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

🔑 Demo Authentication
Token Endpoint
POST /token

Demo Credentials
username: soniya
password: 1234


👉 Use the Authorize button in Swagger UI and paste the token to access protected endpoints.

📁 Project Structure
secure-health-assistant/
├── backend/
│   └── app/
│       ├── main.py                # FastAPI entry point
│       ├── routes/
│       │   ├── auth.py            # OAuth2 authentication
│       │   ├── patient.py         # Patient data APIs
│       │   ├── vitals.py          # Health vitals APIs
│       │   ├── chatbot.py         # Chatbot endpoint (demo)
│       │   ├── imaging_proxy.py   # Medical imaging (stub)
│       │   ├── ocr_proxy.py        # OCR (demo)
│       │   ├── stt_proxy.py        # Speech-to-text (demo)
│       │   ├── ner_proxy.py        # NER (demo)
│       │   └── blockchain_proxy.py
│       └── utils/
│           └── load_data.py        # CSV loaders
├── data/
│   ├── patient_info.csv
│   ├── medical_history.csv
│   ├── health_vitals.csv
│   └── doctor_recommendations.csv
├── contracts/
│   └── SimpleStorage.sol           # Solidity demo contract
├── notebooks/
│   ├── fine_tune_biobert.ipynb
│   └── train_imaging.ipynb
├── requirements.txt
├── .gitignore
└── README.md

⚠️ Disclaimer

This project is for educational and demonstration purposes only.
It does not provide real medical diagnosis or treatment.

👩‍💻 Author

Soniya Surampudi
Master’s Student – Computer Science
Focus: Data Science, AI/ML, Secure Backend Systems

GitHub: https://github.com/soniya487


---




