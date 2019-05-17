from util.random import generator, random_bool
from models.customer import Customer


def build_customer():
    name = generator.first_name_female() if random_bool() else generator.first_name_male()

    return Customer(name=name)
