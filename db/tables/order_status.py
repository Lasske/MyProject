from sqlalchemy import Column, String

from ..base import Base


class OrderStatus(Base):
    __tablename__ = "orders_statuses"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
