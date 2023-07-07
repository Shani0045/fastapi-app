from sqlalchemy import BigInteger, Column, Computed, DateTime, Identity, Integer, Numeric, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Fuelgate(Base):
    __tablename__ = 'fuelgate'

    fuelid = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    vehicleno = Column(Text)
    slipno = Column(Text)
    challanno = Column(Text)
    quantity = Column(Numeric(18, 3))
    fueltime = Column(DateTime)
    vehicleid = Column(Integer)
    fuelslipno = Column(Text, Computed("lpad((fuelid)::text, 8, '0'::text)", persisted=True))
    username = Column(Text)
    slipid = Column(Integer)
    transporter = Column(Text)
    transporterid = Column(Integer)
    location = Column(Text)
    locationid = Column(Integer)
    wheeler = Column(Integer)
    driver = Column(Text)
    driverid = Column(Integer)
    fuelbyrule = Column(Numeric(18, 3))
