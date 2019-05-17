from datetime import timedelta
from util.random import generator, random_bool, random_digits
from models.passport import Passport, Sex


def build_passport():
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
    place_of_birth_format = u'Россия, {city}'
    authority_format = u'ФМС {code}-{number}'
    authority = authority = authority_format.format(code=random_digits(3), number=random_digits(3))
    issued_at = date_of_birth + timedelta(days=generator.random_int(min=14 * 365, max=18 * 365))

    return Passport(name=name,
                    surname=surname,
                    patronymic=patronymic,
                    passport_series=str(generator.random_number(4)),
                    passport_number=str(generator.random_number(6)),
                    date_of_birth=date_of_birth,
                    place_of_birth=place_of_birth_format.format(city=generator.city_name()),
                    sex=sex,
                    authority=authority,
                    issued_at=issued_at)
