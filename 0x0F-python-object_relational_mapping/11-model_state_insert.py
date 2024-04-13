#!/usr/bin/python3
"""adding object to database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def alchemist():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()
    res = session.query(State).filter(State.name == "Louisiana")
    print("{}".format(res[0].id))


if __name__ == '__main__':
    alchemist()
