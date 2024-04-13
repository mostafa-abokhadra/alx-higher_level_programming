#!/usr/bin/python3
"""delete states contain letter a
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
    res = session.query(State).all()
    for item in res:
        if item.name.find('a') != -1:
            session.delete(item)
            session.commit()


if __name__ == "__main__":
    alchemy()
