
from fastapi import APIRouter
from app.routers.dms import router as dms_routers
from app.routers.masters import router as drivers_routers

api_router = APIRouter()

api_router.include_router(dms_routers, prefix="/dms")
api_router.include_router(drivers_routers, prefix="/masters")