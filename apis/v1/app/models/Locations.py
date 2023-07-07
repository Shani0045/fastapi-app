from sqlalchemy import Column, Date, Identity, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Locations(Base):
    __tablename__ = 'locations'

    locationid = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    location = Column(Text)
    locationcode = Column(Text)
    createdate = Column(Date)
