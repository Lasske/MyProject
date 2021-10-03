from sqlalchemy import Column, String, ForeignKey

from ..base import Base


class WheelFormula(Base):
    __tablename__ = "wheels_formula"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    modification_id = Column(
        String(50),
        ForeignKey("modification.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
