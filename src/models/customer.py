from .base import Base
from sqlalchemy import Column, Unicode


class Customer(Base):
    name = Column(Unicode(255), nullable=False)
