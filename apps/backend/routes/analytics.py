from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AnalyticsRequestModel(BaseModel):
    param1: str
    param2: int

class AnalyticsResponseModel(BaseModel):
    message: str
    data: dict

@router.get("/", response_model=AnalyticsResponseModel)
async def get_analytics(request: AnalyticsRequestModel):
    return AnalyticsResponseModel(message="Analytics data", data={"param1": request.param1, "param2": request.param2})
