from sqlalchemy import Column, Integer, String, ForeignKey

from ..base import Base


class OrderModel(Base):
    __tablename__ = "order_models"
    orders_id = Column(
        Integer, ForeignKey("orders.id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True, nullable=False
        )
    models_id = Column(
        String(50), ForeignKey("models.id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True, nullable=False
    )
    count = Column(Integer, nullable=False)
