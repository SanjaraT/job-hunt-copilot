from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

from app.db import create_user, get_user_by_email, get_user_by_id
from app.auth.password import hash_password, verify_password
from app.auth.jwt_utils import create_access_token, decode_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme =OAuth2PasswordBearer(tokenUrl="/auth/login")

class SignupRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/signup", response_model=TokenResponse)
def login(body: LoginRequest):
    user = get_user_by_email(body.email)
    invalid_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
    )

    if not user:
        raise invalid_credentials
    if not verify_password(body.password, user["hashed_password"]):
        raise invalid_credentials

    token = create_access_token(user["id"])
    return TokenResponse(access_token = token)

def get_current_user(token: str = Depends(oauth2_scheme))->dict:

    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)
    if payload is None:
        raise unauthorized

    user_id = payload.get("sub")
    if user_id is None:
        raise unauthorized

    user = get_user_by_id(int(user_id))
    if user is None:
        raise unauthorized

    return user