#!/usr/bin/python3
"""printing all cities
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def alchemy_city():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    for c, s in res:
        print("{}: ({}) {}".format(
            s.name, c.id, c.name))


if __name__ == '__main__':
    alchemy_city()
