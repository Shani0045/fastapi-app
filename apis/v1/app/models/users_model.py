
from sqlalchemy import *
from app.configs.db_config import Base

class Employees(Base):
    __tablename__ = "employees"
    id          =   Column(Integer, primary_key=True)
    name        =   Column(String(50))
    manager_id  =   Column(Integer)

