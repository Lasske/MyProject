from sqlalchemy import Column, String
from ..base import Base


class CarBody(Base):
    __tablename__ = "car_bodies"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
