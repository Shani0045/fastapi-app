from sqlalchemy import Boolean, Column, Date, Identity, Integer, Text, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Owners(Base):
    __tablename__ = 'owners'

    ownerid = Column(Integer, Identity(always=True, start=83, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    ownername = Column(Text)
    address1 = Column(Text)
    address2 = Column(Text)
    pan = Column(Text)
    aadhar = Column(Text)
    mobile = Column(Text)
    gst = Column(Text)
    startdate = Column(Date)
    enddate = Column(Date)
    dlno = Column(Text)
    isactive = Column(Boolean, server_default=text('true'))
    status = Column(Text)
    statuschangedate = Column(Date)
    stateid = Column(Integer)
    state = Column(Text)
    pincode = Column(Text)
    bankname = Column(Text)
    accountno = Column(Text)
    ifsc = Column(Text)
    transportercode = Column(Text)
