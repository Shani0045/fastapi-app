
from fastapi import APIRouter, Query, Depends
from fastapi.responses import Response
from sqlalchemy import text

from app.configs.db_config import  get_db

from app.models.Ingate import Ingate


# Create your routes here

router = APIRouter(tags=["DMS APIs"])

@router.get("/ingate/", description="list of ingate")
async def ingate(
    pg_conn = Depends(get_db)
):

    data= pg_conn.query(Ingate).all()

    return {"ingate":data}






