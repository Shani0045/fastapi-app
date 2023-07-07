

from fastapi import APIRouter, Depends, Form
from fastapi.responses import Response

from app.configs.db_config import  get_db

from app.models.Drivers import Drivers
from app.models.Locations import Locations
from app.models.Owners import Owners
from app.models.FuelMaster import Fuelmaster
from app.models.Weighbridge import Weighbridge

from app.schemas.DriversSchema import DriversGetResponse, DriverPostResponse, DriversSchema

# Create your routes here

router = APIRouter(tags=["Masters APIs"])

# drivers get route here
@router.get("/drivers/", description="list of drivers")
async def drivers(
    session = Depends(get_db)
):

    data = session.query(Drivers).all()
    response = DriversGetResponse(drivers=data)

    return response

# drivers post route here
@router.post("/add-drivers/", description="new drivers add")
async def adddrivers(
    session              =  Depends(get_db),
    drivername:str       =  Form(None),
    dlno: str            =  Form(None),
    dltype: str          =  Form(None),
    address: str         =  Form(None),
    dlexpiry: str        =  Form(None),
    isactive: bool       =  Form(None),
    drivermobile: str    =  Form(None),
    fingerprint: str     =  Form(None),
    faceprint: str       =  Form(None),
    status: str          =  Form(None),
    statuschangedate: str = Form(None),
):
    
    drivers = Drivers(
        drivername = drivername, 
        dlno = dlno, 
        dltype = dltype, 
        address = address,
        dlexpiry = dlexpiry, 
        isactive = isactive,
        drivermobile = drivermobile,
        fingerprint = fingerprint,
        faceprint = faceprint,
        status = status,
        statuschangedate = statuschangedate
    )

    drivers.save(session)
    
    return DriverPostResponse(msg="Successfully added", status_code=201)

# locations route here
@router.get("/locations/", description="list of locations")
async def locations(
    session = Depends(get_db)
):

    data= session.query(Locations).all()

    return {"locations":data}

# owners route here
@router.get("/owners/", description="list of owners")
async def owners(
    session = Depends(get_db)
):

    data= session.query(Owners).all()

    return {"owners":data}

# fuels route here
@router.get("/fuels/", description="list of fuels")
async def fuels(
    session = Depends(get_db)
):

    data= session.query(Fuelmaster).all()

    return {"fuels":data}

@router.get("/weighbridge/", description="list of weighbridge")
async def owners(
    session = Depends(get_db)
):

    data= session.query(Weighbridge).all()

    return {"owners":data}
