
from fastapi import FastAPI
import os

from app.routers import api_router
from app.config import conf
 
# main app start here

API_TITLE =  "Dispach Management System"
API_VERSION = conf.API_VERSION
DESCRIPTION = "dispach management system api version "+API_VERSION

DOCS_URL = "/test-apis" if os.getenv("PYTHON_ENV") in ["dev", "development", "test"] else None
REDOC_URL = "/"  if os.getenv("PYTHON_ENV") in ["dev", "development", "test"] else None

app = FastAPI(
        title =API_TITLE,
        description = DESCRIPTION ,
        version = API_VERSION,
        docs_url = DOCS_URL ,
        redoc_url = REDOC_URL
    )

app.include_router(api_router)
