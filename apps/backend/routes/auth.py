from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AuthRequestModel(BaseModel):
    username: str
    password: str

class AuthResponseModel(BaseModel):
    message: str

@router.post("/login", response_model=AuthResponseModel)
async def login(request: AuthRequestModel):
    return AuthResponseModel(message="User logged in")

@router.post("/register", response_model=AuthResponseModel)
async def register(request: AuthRequestModel):
    return AuthResponseModel(message="User registered")
