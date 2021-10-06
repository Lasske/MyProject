from sqlalchemy import Column, Integer, DATETIME, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    sale_date = Column(DATETIME, nullable=False)
    user_login = Column(
        String(50),
        ForeignKey("users.login", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    order_status_id = Column(
        String(50),
        ForeignKey("orders_statuses.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    user = relationship("User")
    order_status = relationship("OrderStatus")
