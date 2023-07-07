
from fastapi import APIRouter, Query, Depends
from fastapi.responses import Response
from sqlalchemy import text

from app.configs.db_config import  get_db

from app.schemas.users_schema import Users
from app.models.users_model import Employees
from app.modules.users.get_all_users import get_users


# Create your routes here

router = APIRouter(tags=["Users"])

@router.get("/users/")
async def list_users(
    pg_conn = Depends(get_db)
):

    data= pg_conn.query(Employees).all()

    return {"employees":data}

