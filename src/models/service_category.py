from .base import Base
from sqlalchemy import Column, Integer, Unicode, Index
from sqlalchemy.orm import relation


class ServiceCategory(Base):
    """
        ServiceCategory model implements NestedSet tree storage algorithm, see:

        * https://docs.sqlalchemy.org/en/13/_modules/examples/nested_sets/nested_sets.html
        * https://habr.com/ru/post/46659/
        * http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/
        * https://www.sitepoint.com/hierarchical-data-database/
        * http://www.klempert.de/nested_sets/
        * http://www.ibase.ru/files/articles/programming/dbmstrees/sqltrees.html
    """
    __table_args__ = (Index('nested_set_idx', 'left_node', 'right_node'), Base.__table_args__)

    name = Column(Unicode(255), nullable=False)
    node_level = Column(Integer, nullable=False)
    left_node = Column(Integer, nullable=False)
    right_node = Column(Integer, nullable=False)

    services = relation('Service', back_populates='category', cascade='all, delete, delete-orphan')
