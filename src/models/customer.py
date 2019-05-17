from .base import Base
from sqlalchemy import Column, Unicode
from sqlalchemy.orm import relation


class Customer(Base):
    name = Column(Unicode(255), nullable=False)

    orders = relation('Order', back_populates='customer', cascade='all, delete, delete-orphan')
