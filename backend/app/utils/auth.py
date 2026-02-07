import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

JWT_SECRET = os.environ.get("JWT_SECRET", "secret")
JWT_ALGO = os.environ.get("JWT_ALGORITHM", "HS256")

# for demo: in-memory users
fake_users = {
    "doctor@example.com": {"username":"doctor@example.com","full_name":"Dr. Alice","role":"doctor"},
    "patient@example.com": {"username":"patient@example.com","full_name":"Bob","role":"patient"},
    "admin@example.com": {"username":"admin@example.com","full_name":"Admin","role":"admin"},
}

def create_token(subject: str, role: str, expires_minutes: int = 60):
    payload = {"sub": subject, "role": role, "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)

def decode_token(token: str):
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return data
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    data = decode_token(token)
    username = data.get("sub")
    if username in fake_users:
        u = fake_users[username]
        u["role"] = data.get("role")
        return u
    raise HTTPException(status_code=401, detail="User not found")
