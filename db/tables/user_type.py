from sqlalchemy import Column, String

from ..base import Base


class UserType(Base):
    __tablename__ = "users_types"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
