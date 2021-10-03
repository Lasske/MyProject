from sqlalchemy import Column, String, ForeignKey

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
