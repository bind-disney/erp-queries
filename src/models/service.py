from .base import Base
from .service_category import ServiceCategory
from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relation, backref


class Service(Base):
    name = Column(Unicode(255), nullable=False)
    category_id = Column(Integer,
                         ForeignKey('service_categories.id', ondelete='CASCADE', onupdate='RESTRICT'),
                         index=True,
                         nullable=False)

    category = relation(ServiceCategory, backref=backref('services'), primaryjoin=ServiceCategory.id == category_id)
