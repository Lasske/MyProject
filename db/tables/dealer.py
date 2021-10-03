from sqlalchemy import Column, String, ForeignKey

from ..base import Base


class Dealer(Base):
    __tablename__ = "dealers"
    login = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(50), nullable=False)
    user_type_id = Column(
        String(50),
        ForeignKey("users_types.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
