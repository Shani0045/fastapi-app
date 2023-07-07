from sqlalchemy import Column, Identity, Integer, Numeric, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Weighbridge(Base):
    __tablename__ = 'weighbridge'

    wbid = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    wbname = Column(Text, nullable=False)
    locationid = Column(Integer)
    location = Column(Text)
    capacity = Column(Numeric(18, 3))
