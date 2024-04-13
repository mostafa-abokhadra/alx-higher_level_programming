#!/usr/bin/python3
"""improving city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """city class for city dbase
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
