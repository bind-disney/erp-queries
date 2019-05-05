import enum
from .base import Base
from sqlalchemy import Column, Integer, Unicode, CHAR, Date, Enum, UniqueConstraint


class Sex(enum.Enum):
    male = 'M'
    female = 'F'


class Passport(Base):
    __table_args__ = (UniqueConstraint('passport_series', 'passport_number', name='passport_uniq'), Base.__table_args__)

    id = Column(Integer, primary_key=True)
    passport_series = Column(CHAR(4), nullable=False)
    passport_number = Column(CHAR(6), nullable=False)
    name = Column(Unicode(255), nullable=False)
    surname = Column(Unicode(255), nullable=False)
    patronymic = Column(Unicode(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    place_of_birth = Column(Unicode(255), nullable=False)
    sex = Column(Enum(Sex), nullable=False)
    issued_at = Column(Date, nullable=False)
    authority = Column(Unicode(255), nullable=False)
