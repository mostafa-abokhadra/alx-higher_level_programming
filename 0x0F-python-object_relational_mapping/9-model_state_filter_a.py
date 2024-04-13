#!/usr/bin/python3

"""states that contain letter a
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def alchemist_connection():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id).all()
    for data in res:
        if data.name.find('a') != -1:
            print("{}: {}".format(data.id, data.name))


if __name__ == '__main__':
    alchemist_connection()
