from .base import Base
from .passport import Passport
from sqlalchemy import Column, Integer, DECIMAL, Unicode, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Contractor(Base):
    name = Column(Unicode(255), nullable=False)
    surname = Column(Unicode(255), nullable=False)
    patronymic = Column(Unicode(255), nullable=False)
    rating = Column(DECIMAL(5, 2), nullable=False, default=0.0)
    email = Column(Unicode(100), unique=True, index=True, nullable=False)
    phone_number = Column(Unicode(20), unique=True, index=True, nullable=False)
    email_confirmed_at = Column(DateTime)
    phone_number_confirmed_at = Column(DateTime)
    passport_id = Column(Integer,
                         ForeignKey('passports.id', ondelete='CASCADE', onupdate='RESTRICT'),
                         index=True,
                         nullable=False)

    passport = relationship(Passport, backref='contractor', primaryjoin=Passport.id == passport_id)
