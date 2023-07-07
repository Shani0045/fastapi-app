from sqlalchemy import Column, DateTime, Identity, Integer, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Fuelmaster(Base):
    __tablename__ = 'fuelmaster'

    fuelid = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    wheels = Column(Integer)
    fuelpermt = Column(Numeric(18, 3))
    effectivefrom = Column(DateTime)
