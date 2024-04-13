#!/usr/bin/python3

"""importving city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """city class for citis table
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
