import enum
from .base import Base
from .order import Order
from .service_category import ServiceCategory
from sqlalchemy import Column, Integer, UnicodeText, Enum, ForeignKey
from sqlalchemy.orm import relation, backref


class ReviewType(enum.Enum):
    badly = 1
    unsatisfactorily = 2
    satisfactorily = 3
    good = 4
    excellently = 5


class Review(Base):
    order_id = Column(Integer,
                      ForeignKey('orders.id', ondelete='CASCADE', onupdate='RESTRICT'),
                      index=True,
                      nullable=False)
    service_category_id = Column(Integer,
                                 ForeignKey('service_categories.id', ondelete='CASCADE', onupdate='RESTRICT'),
                                 index=True,
                                 nullable=False)
    order_category_id = Column(Integer,
                               ForeignKey('service_categories.id', ondelete='CASCADE', onupdate='RESTRICT'),
                               index=True,
                               nullable=False)
    review_type = Column(Enum(ReviewType), index=True, nullable=False)
    content = Column(UnicodeText(4000), nullable=False)

    order = relation(Order, backref=backref('reviews'), primaryjoin=Order.id == order_id)
    order_category = relation(ServiceCategory, primaryjoin=ServiceCategory.id == order_category_id)
    service_category = relation(ServiceCategory, primaryjoin=ServiceCategory.id == service_category_id)
