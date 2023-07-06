
from fastapi import APIRouter
from app.routers.users import router as user_routers

api_router = APIRouter()

api_router.include_router(user_routers, prefix="/users")
