from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_identity():
    return {"message": "Identity data"}
