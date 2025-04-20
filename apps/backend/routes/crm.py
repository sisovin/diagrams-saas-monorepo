from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_crm():
    return {"message": "CRM data"}
