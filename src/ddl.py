# -*- coding: utf-8

from sqlalchemy.orm import sessionmaker
from models import establish_connection, Base

engine = establish_connection()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# TODO: generate your objects here from factories...

session.commit()
session.close()
