from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequestModel(BaseModel):
    message: str

class ChatResponseModel(BaseModel):
    response: str

@router.get("/", response_model=ChatResponseModel)
async def get_chat(request: ChatRequestModel):
    return ChatResponseModel(response="Chat data")
