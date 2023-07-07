
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname("v1"),'.env'))

class Config:
    """ write environment variables here"""

    PYTHON_ENV = os.getenv("PYTHON_ENV")
    API_VERSION = os.getenv("API_VERSION")


# Initialize config instance

conf = Config()

