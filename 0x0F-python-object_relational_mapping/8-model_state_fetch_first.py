#!/usr/bin/python3

"""listing the first object
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def alchemist_connection():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        res = session.query(State).first()
        print("{}: {}".format(res.id, res.name))
    except Exception:
        print("Nothing")
        return 0


if __name__ == '__main__':
    alchemist_connection()
