from sqlalchemy import Column, String, ForeignKey

from ..base import Base


class CarBody(Base):
    __tablename__ = "car_bodyes"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    modification_id = Column(
        String(50),
        ForeignKey("modification.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
