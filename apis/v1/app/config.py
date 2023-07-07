
from dotenv import load_dotenv
import os
from app.custom_exceptions.custom import EnvError

env = load_dotenv(os.path.join(os.path.dirname("v1"),'.env'))

if not env:
    raise EnvError(".env file not found or not fully loaded...")

class Config:
    """ write environment variables here"""

    PYTHON_ENV = os.getenv("PYTHON_ENV")
    API_VERSION = os.getenv("API_VERSION")


# Initialize config instances

conf = Config()
