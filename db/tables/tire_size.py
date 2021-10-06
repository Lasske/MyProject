from sqlalchemy import Column, String


from ..base import Base


class TireSize(Base):
    __tablename__ = "tire_sizes"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)