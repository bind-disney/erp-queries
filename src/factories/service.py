from util.random import generator
from models.service import Service


def build_service(category):
    return Service(name=generator.sentence(3), category=category)
