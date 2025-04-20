from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class IdentityRequestModel(BaseModel):
    param1: str
    param2: int

class IdentityResponseModel(BaseModel):
    message: str
    data: dict

@router.get("/", response_model=IdentityResponseModel)
async def get_identity(request: IdentityRequestModel):
    return IdentityResponseModel(message="Identity data", data={"param1": request.param1, "param2": request.param2})
