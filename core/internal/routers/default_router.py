from fastapi import APIRouter

from core.infrastructure.database import db_manager

router = APIRouter(tags=["Default"])

@router.get("/")
async def get_all():
    return ["Item 1", "Item 2"]