from fastapi import FastAPI
from pydantic import BaseModel
from django.conf import settings as sett
from django.contrib.auth.hashers import make_password, check_password
import django
from config_data.config import settings


class PasswordRequest(BaseModel):
    password: str


class PasswordResponse(BaseModel):
    hashed_password: str


class PasswordCheckRequest(BaseModel):
    password: str
    hashed_password: str


class PasswordCheckResponse(BaseModel):
    is_valid: bool


app = FastAPI()


sett.configure(
    SECRET_KEY=settings.secret_key,
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
    ],
)
django.setup()


@app.post("/encrypt/", response_model=PasswordResponse)
async def encrypt_password(request: PasswordRequest):
    hashed_password = make_password(request.password)
    return PasswordResponse(hashed_password=hashed_password)


@app.post("/check/", response_model=PasswordCheckResponse)
async def check_password_validity(request: PasswordCheckRequest):
    is_valid = check_password(request.password, request.hashed_password)
    return PasswordCheckResponse(is_valid=is_valid)
