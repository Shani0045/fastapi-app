from sqlalchemy import BigInteger, Column, DateTime, Identity, Integer, Numeric, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Outgate(Base):
    __tablename__ = 'outgate'

    challanid = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    slipno = Column(Text)
    slipid = Column(BigInteger)
    vehicleno = Column(Text)
    driver = Column(Text)
    driverid = Column(BigInteger)
    loading = Column(Text)
    destination = Column(Text)
    challanno = Column(Text)
    gross = Column(Numeric(18, 3))
    tare = Column(Numeric(18, 3))
    net = Column(Numeric(18, 3))
    passdate = Column(DateTime)
    passgate = Column(Text)
    sliptime = Column(DateTime)
    challantime = Column(DateTime)
    printtime = Column(DateTime)
    material = Column(Text)
    weighbridge = Column(Text)
    vehicleid = Column(Integer)
    locationid = Column(Integer)
    username = Column(Text)
    transporterid = Column(Integer)
    transporter = Column(Text)
    challannet = Column(Numeric(18, 3))
    grosswbid = Column(Integer)
    grosswb = Column(Text)
    tarewbid = Column(Integer)
    tarewb = Column(Text)
    passoperator = Column(Text)
    wbdatetime = Column(DateTime)
