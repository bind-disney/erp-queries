# -*- coding: utf-8

import sys
from datetime import timedelta
from sqlalchemy.orm import sessionmaker
from util.random import generator, random_bool, random_digits
from models import establish_connection, Base, Passport, Sex, Contractor, Customer
from models import ServiceCategory, Service, Order, OrderStatus, Review, ReviewType

engine = establish_connection()
Base.metadata.create_all(engine)

sys.exit()

Session = sessionmaker(bind=engine)
session = Session()

place_of_birth_format = u'Россия, {city}'
authority_format = u'ФМС {code}-{number}'

contractors_count = 1
customers_count = 1

for i in range(contractors_count):
    if random_bool():
        sex = Sex.female
        name = generator.first_name_female()
        surname = generator.last_name_female()
        patronymic = generator.middle_name_female()
    else:
        sex = Sex.male
        name = generator.first_name_male()
        surname = generator.last_name_male()
        patronymic = generator.middle_name_male()

    date_of_birth = generator.date_of_birth()
    issued_at = date_of_birth + timedelta(days=generator.random_int(min=14 * 365, max=18 * 365))
    place_of_birth = place_of_birth_format.format(city=generator.city_name())
    authority = authority_format.format(code=random_digits(3), number=random_digits(3))
    rating = generator.pyfloat(left_digits=1, right_digits=2, positive=True, min_value=0.0, max_value=5.0)
    email_confirmed_at = generator.past_datetime() if random_bool() else None
    phone_number_confirmed_at = generator.past_datetime() if random_bool() else None

    passport = Passport(passport_series=str(generator.random_number(4)),
                        passport_number=str(generator.random_number(6)),
                        name=name,
                        surname=surname,
                        patronymic=patronymic,
                        date_of_birth=date_of_birth,
                        place_of_birth=place_of_birth,
                        sex=sex,
                        authority=authority,
                        issued_at=issued_at)

    contractor = Contractor(name=name,
                            surname=surname,
                            patronymic=patronymic,
                            rating=rating,
                            email=generator.email(),
                            phone_number=generator.phone_number(),
                            email_confirmed_at=email_confirmed_at,
                            phone_number_confirmed_at=phone_number_confirmed_at,
                            passport=passport)

    session.add(passport)
    session.add(contractor)

for i in range(customers_count):
    customer = Customer(name=generator.name())
    session.add(customer)

session.commit()
session.close()
