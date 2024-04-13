#!/usr/bin/python3
"""changing name
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def alchemy():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter(State.id == 2)
    obj[0].name = 'New Mexico'
    session.commit()


if __name__ == '__main__':
    alchemy()
