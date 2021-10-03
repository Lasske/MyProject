from sqlalchemy import Column, Integer, DATETIME, String, ForeignKey

from ..base import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    sale_date = Column(DATETIME, nullable=False)
    dealer_login = Column(
        String(50),
        ForeignKey("dealers.login", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    order_status_id = Column(
        String(50),
        ForeignKey("order_status.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
