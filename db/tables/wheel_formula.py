from sqlalchemy import Column, String


from ..base import Base


class WheelFormula(Base):
    __tablename__ = "wheels_formulas"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
