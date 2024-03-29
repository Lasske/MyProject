from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class User(Base):
    __tablename__ = "users"
    login = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(50), nullable=False)
    user_type_id = Column(
        String(50),
        ForeignKey("users_types.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )

    user_type = relationship("UserType")
