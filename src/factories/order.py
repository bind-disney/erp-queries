from random import choice
from util.random import generator, random_bool
from models.order import Order, OrderStatus


def build_order(service, customer, contractor):
    return Order(service=service,
                 customer=customer,
                 contractor=contractor,
                 status=random_status(),
                 license_required=random_bool(),
                 priority=generator.random_number(1))


def random_status():
    return choice(list(map(str, OrderStatus.__members__)))
