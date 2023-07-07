from sqlalchemy import BigInteger, Boolean, Column, Date, Identity, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Drivers(Base):
    __tablename__ = 'drivers'

    driverid = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    drivername = Column(Text)
    dlno = Column(Text, unique=True)
    dltype = Column(Text)
    address = Column(Text)
    dlexpiry = Column(Date)
    isactive = Column(Boolean)
    drivermobile = Column(Text)
    fingerprint = Column(Text)
    faceprint = Column(Text)
    status = Column(Text)
    statuschangedate = Column(Date)

    def save(self, session):
        session.add(self)
        session.commit()
