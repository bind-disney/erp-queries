from .base import Base
from .service_category import ServiceCategory
from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relation


class Service(Base):
    name = Column(Unicode(255), nullable=False)
    category_id = Column(Integer,
                         ForeignKey('service_categories.id', ondelete='CASCADE', onupdate='RESTRICT'),
                         index=True,
                         nullable=False)

    category = relation('ServiceCategory', back_populates='services', primaryjoin=ServiceCategory.id == category_id)
    orders = relation('Order', back_populates='service', cascade='all, delete, delete-orphan')
