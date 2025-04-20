from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FilesRequestModel(BaseModel):
    param1: str
    param2: int

class FilesResponseModel(BaseModel):
    message: str
    data: dict

@router.get("/", response_model=FilesResponseModel)
async def get_files(request: FilesRequestModel):
    return FilesResponseModel(message="Files data", data={"param1": request.param1, "param2": request.param2})
