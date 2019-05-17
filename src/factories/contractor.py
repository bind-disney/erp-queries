from util.random import generator, random_bool
from models.contractor import Contractor


def build_contractor(passport):
    rating = generator.pyfloat(left_digits=1, right_digits=2, positive=True, min_value=0.0, max_value=5.0)

    email_confirmed_at = generator.past_datetime() if random_bool() else None
    phone_number_confirmed_at = generator.past_datetime() if random_bool() else None

    return Contractor(name=passport.name,
                      surname=passport.surname,
                      patronymic=passport.patronymic,
                      rating=rating,
                      email=generator.email(),
                      phone_number=generator.phone_number(),
                      email_confirmed_at=email_confirmed_at,
                      phone_number_confirmed_at=phone_number_confirmed_at,
                      passport=passport)
