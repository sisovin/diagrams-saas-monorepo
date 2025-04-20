from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CRMRequestModel(BaseModel):
    param1: str
    param2: int

class CRMResponseModel(BaseModel):
    message: str
    data: dict

@router.get("/", response_model=CRMResponseModel)
async def get_crm(request: CRMRequestModel):
    return CRMResponseModel(message="CRM data", data={"param1": request.param1, "param2": request.param2})
