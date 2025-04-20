from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class GenericRequestModel(BaseModel):
    param1: str
    param2: int

class GenericResponseModel(BaseModel):
    message: str
    data: dict

@router.get("/", response_model=GenericResponseModel)
async def get_generic(request: GenericRequestModel):
    return GenericResponseModel(message="Generic data", data={"param1": request.param1, "param2": request.param2})
