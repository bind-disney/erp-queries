from faker import Faker

generator = Faker('ru_RU')


def random_bool():
    global generator
    return generator.random_number(1) > 1


def random_digits(count=3):
    global generator
    return str(generator.random_number(count)).rjust(count, '0')
