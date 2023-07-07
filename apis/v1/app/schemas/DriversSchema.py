
from pydantic import BaseModel
from typing import List

class DriversSchema(BaseModel):
    driverid:int| None
    drivername:str | None
    dlno:str |None
    dltype:str |None
    address:str |None
    dlexpiry:str |None
    isactive:bool |None
    drivermobile :str |None
    fingerprint :str |None
    faceprint :str |None
    status :str |None
    statuschangedate:str |None

class DriversGetResponse(BaseModel):
    drivers:list|None = List[DriversSchema]

class DriverPostResponse(BaseModel):
    msg:str
    status_code:int