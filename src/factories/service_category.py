from util.random import generator
from models.service_category import ServiceCategory


def build_service_category():
    left_node = generator.random_number(1)
    right_node = left_node + generator.random_number(1)

    return ServiceCategory(name=generator.sentence(3),
                           node_level=generator.random_number(1),
                           left_node=left_node,
                           right_node=right_node)
