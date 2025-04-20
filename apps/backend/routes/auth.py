from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"message": "User logged in"}

@router.post("/register")
async def register():
    return {"message": "User registered"}
