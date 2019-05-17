from sqlalchemy import or_, func, desc
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker, aliased, selectinload, joinedload, contains_eager
from models import establish_connection, Contractor, Passport, ServiceCategory, Service

engine = establish_connection()
Session = sessionmaker()
session = Session(bind=engine)

# contractor = session.query(Contractor).filter_by(name='foo').first()

# for c in session.query(Contractor).filter_by(name='foo').order_by(Contractor.id)[1:3]:
#     print(c)

# contractor_ids = session.query(Contractor.id.label('id')).order_by(Contractor.created_at).filter(
#     or_(Contractor.email_confirmed_at.isnot(None), Contractor.phone_number_confirmed_at.isnot(None))).all()

# print(contractor_ids)

# contractors_count = session.query(func.count(Contractor.id).label('contractors_count')).scalar()

# print(contractors_count)

# for id, name in session.query(Contractor.id, Contractor.name).order_by(desc(Contractor.created_at)).all():
#     print(id, name)

# contractor, passport = session.query(Contractor, Passport).join(Passport).filter(Contractor.id == 1).one()

# statement = session.query(Contractor.passport_id, func.count('*').label('passports_count')).\
#     group_by(Contractor.passport_id).subquery()

# for contractor_id, passports_count in session.query(Contractor.id, statement.c.passports_count).\
#                                                     join(statement, Contractor.passport_id == statement.c.passport_id).\
#                                                     order_by(Contractor.passport_id):
#     print(contractor_id, passports_count)

# statement = session.query(Passport.id).filter(Passport.passport_series == '8292', Passport.passport_number == '174819').subquery()
# passport_alias = aliased(Passport, statement)

# for contractor, passport in session.query(Contractor, passport_alias).join(passport_alias):
#     print(contractor.id, contractor.passport_id)
#     print(passport.id)


# statement = exists([Passport.id]).where(Contractor.passport_id == Passport.id)

# for name, in session.query(Contractor.name).filter(statement):
#     print(name)


# for name, in session.query(ServiceCategory.name).filter(ServiceCategory.services.any()):
#     print(name)


# for name, in session.query(ServiceCategory.name).filter(ServiceCategory.services.any(Service.name.ilike('%cleaning%'))):
#     print(name)


# session.query(Service).filter(Service.category.has(ServiceCategory.node_level==2)).all()


# service_category = ServiceCategory(name='Cleaning', left_node=0, right_node=1, node_level=0)
# service_1 = Service(name='Wet cleaning of premises', category=service_category)
# service_2 = Service(name='Windows washing', category=service_category)
# session.add(service_category)
# session.add(service_1)
# session.add(service_2)
# session.commit()

# service_category = session.query(ServiceCategory).options(selectinload(ServiceCategory.services)).\
#     filter_by(name='Cleaning').first()

# if service_category:
#     for service in service_category.services:
#         print(service.name)


# services = session.query(Service).\
#     join(Service.category).\
#     filter(ServiceCategory.name == 'Cleaning').\
#     options(contains_eager(Service.category)).\
#     all()

# for service in services:
#     print(service.name)
