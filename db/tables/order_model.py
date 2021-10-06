from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class OrderModel(Base):
    __tablename__ = "order_models"
    order_id = Column(
        Integer, ForeignKey("orders.id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True, nullable=False
        )
    model_id = Column(
        String(50), ForeignKey("models.id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True, nullable=False
    )
    count = Column(Integer, nullable=False)

    order = relationship("Order")
    model = relationship("Model")
