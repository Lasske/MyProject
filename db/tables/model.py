from sqlalchemy import Column, String, DECIMAL

from ..base import Base


class Model(Base):
    __tablename__ = "models"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    price = Column(DECIMAL(7, 2), nullable=False)
    description = Column(String(255), nullable=False)
