from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

router = APIRouter(prefix="", tags=["Auth"])

# demo secret for local testing (move to .env later)
SECRET_KEY = "dev-secret-key"
ALGORITHM = "HS256"

# demo "users"
DEMO_USERS = {
    "soniya": {"password": "1234", "role": "doctor", "patient_id": 1},
    "patient1": {"password": "1234", "role": "patient", "patient_id": 1},
}

@router.post("/token")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = DEMO_USERS.get(form_data.username)

    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    payload = {
        "sub": form_data.username,
        "role": user["role"],
        "patient_id": user["patient_id"],
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}
