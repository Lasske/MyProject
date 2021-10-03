from sqlalchemy import Column, String

from ..base import Base


class PhoneType(Base):
    __tablename__ = "phones_types"
    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
