from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Identity, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Vehicles(Base):
    __tablename__ = 'vehicles'

    vehicleid = Column(Integer, Identity(always=True, start=387, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    vehicleno = Column(Text)
    compliant = Column(Integer)
    ownerid = Column(BigInteger)
    ownername = Column(Text)
    ownermobile = Column(Text)
    rcno = Column(Text)
    tempno = Column(Text)
    chasisno = Column(Text)
    fitnessexpiry = Column(Date)
    insuranceexpiry = Column(Date)
    permitexpiry = Column(Date)
    pollutionexpiry = Column(Date)
    permittype = Column(Text)
    status = Column(Text)
    statuschangedate = Column(Date)
    createdate = Column(Date)
    ownerpan = Column(Text)
    rfno = Column(Text)
    rfid = Column(BigInteger)
    permit = Column(Text)
    insurance = Column(Text)
    pollution = Column(Text)
    fitness = Column(Text)
    isactive = Column(Boolean)
    roadtax = Column(Text)
    roadtaxexpiry = Column(DateTime)
    rcdate = Column(DateTime)
    wheeler = Column(Integer)
    vowner = Column(Text)
    vcontact = Column(Text)
    vaddress = Column(Text)
    vownership = Column(Boolean)
    gpsdate = Column(DateTime)
