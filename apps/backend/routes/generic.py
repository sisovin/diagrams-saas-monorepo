from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_generic():
    return {"message": "Generic data"}
