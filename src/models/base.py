import os
from util.inflector import inflector
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.expression import text
from sqlalchemy.util import clsname_as_plain_name


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return inflector.plural('_'.join(clsname_as_plain_name(cls).split(' ')))

    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': os.getenv('MYSQL_CHARSET', 'utf8mb4')}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=text('NOW()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('NOW()'))


Base = declarative_base(cls=Base)


def create_connection():
    engine_options = {
        'pool_size': 10,
        'max_overflow': 10,
        'case_sensitive': True,
        'convert_unicode': True,
        'echo': True
    }

    return create_engine(database_url(), **engine_options)


def establish_connection():
    engine = create_connection()
    engine.connect()

    return engine


def database_url():
    db_host = os.getenv('MYSQL_HOST')
    db_port = os.getenv('MYSQL_PORT', 3306)
    db_user = os.getenv('MYSQL_USER')
    db_password = os.getenv('MYSQL_PASSWORD')
    db_name = os.getenv('MYSQL_DATABASE')
    db_charset = os.getenv('MYSQL_CHARSET', 'utf8mb4')
    db_url_format = 'mysql+mysqldb://{user}:{password}@{host}:{port}/{name}?charset={charset}'

    return db_url_format.format(user=db_user,
                                password=db_password,
                                host=db_host,
                                port=db_port,
                                name=db_name,
                                charset=db_charset)
