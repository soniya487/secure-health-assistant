from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Auth"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Demo credentials (change later)
    if form_data.username != "Soniya" or form_data.password != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return {"access_token": "demo-token", "token_type": "bearer"}
