
from fastapi import FastAPI

from app.routers import api_router
 

# main app start here

DOCS_URL = "/test-apis" if 1 else None
REDOC_URL = "/"  if 1 else None

API_VERSION = '1.0 Beta' 
API_TITLE =  "Users APIs"
DESCRIPTION = "Users APIs"

app = FastAPI(
        title =API_TITLE,
        description = DESCRIPTION ,
        version = API_VERSION,
        docs_url = DOCS_URL ,
        redoc_url = REDOC_URL
    )

app.include_router(api_router)
