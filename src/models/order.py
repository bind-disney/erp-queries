import enum
from .base import Base
from .service import Service
from .customer import Customer
from .contractor import Contractor
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relation


class OrderStatus(enum.Enum):
    new = 'NEW'
    pending = 'PENDING'
    completed = 'COMPLETED'
    cancelled = 'CANCELLED'


class Order(Base):
    service_id = Column(Integer,
                        ForeignKey('services.id', ondelete='CASCADE', onupdate='RESTRICT'),
                        index=True,
                        nullable=False)
    customer_id = Column(Integer,
                         ForeignKey('customers.id', ondelete='CASCADE', onupdate='RESTRICT'),
                         index=True,
                         nullable=False)
    contractor_id = Column(Integer,
                           ForeignKey('contractors.id', ondelete='CASCADE', onupdate='RESTRICT'),
                           index=True,
                           nullable=False)
    status = Column(Enum(OrderStatus), index=True, nullable=False, default=OrderStatus.new)
    license_required = Column(Boolean, nullable=False)
    priority = Column(Integer, index=True, nullable=False)

    service = relation(Service, back_populates='orders', primaryjoin=Service.id == service_id)
    customer = relation(Customer, back_populates='orders', primaryjoin=Customer.id == customer_id)
    contractor = relation(Contractor, back_populates='orders', primaryjoin=Contractor.id == contractor_id)
