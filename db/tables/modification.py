from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Modification(Base):
    __tablename__ = "modifications"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    model_id = Column(
        String(50),
        ForeignKey("models.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    car_body_id = Column(
        String(50),
        ForeignKey("car_bodies.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    tire_size_id = Column(
        String(50),
        ForeignKey("tire_sizes.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    wheel_formula_id = Column(
        String(50),
        ForeignKey("wheels_formulas.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )

    model = relationship("Model")
    car_body = relationship("CarBody")
    tire_size = relationship("TireSize")
    wheel_formula = relationship("WheelFormula")
