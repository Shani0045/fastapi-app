
from pydantic import BaseModel, Field

class Users(BaseModel):
    username : str 
    age : int
    email : str | None
    mobile : str  | None