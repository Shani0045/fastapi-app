from sqlalchemy import BigInteger, Boolean, Column, Computed, DateTime, Identity, Integer, Numeric, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Ingate(Base):
    __tablename__ = 'ingate'

    slipid = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    sliptime = Column(DateTime)
    vehicleno = Column(Text)
    destination = Column(Text)
    loading = Column(Text)
    dlno = Column(Text)
    transporter = Column(Text)
    gate = Column(Text)
    currentlogin = Column(Text)
    driver = Column(Text)
    controlno = Column(BigInteger)
    driverid = Column(BigInteger)
    tare = Column(Numeric(18, 3))
    rfid = Column(BigInteger)
    rfno = Column(Text)
    locationid = Column(Integer)
    transporterid = Column(Integer)
    vehicleid = Column(Integer)
    validslip = Column(Boolean)
    slipno = Column(Text, Computed("lpad((slipid)::text, 8, '0'::text)", persisted=True))
    quantity = Column(Numeric(18, 3))
    fueltime = Column(DateTime)
    fueloperator = Column(Text)
    wheeler = Column(Integer)
