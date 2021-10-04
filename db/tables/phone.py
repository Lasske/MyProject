from sqlalchemy import Column, String, Integer, ForeignKey

from ..base import Base


class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    number = Column(String(50), nullable=False)
    phone_type_id = Column(
        String(50),
        ForeignKey("phones_types.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    dealer_login = Column(
        String(50),
        ForeignKey("users.login", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
