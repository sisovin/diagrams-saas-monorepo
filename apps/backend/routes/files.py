from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_files():
    return {"message": "Files data"}
