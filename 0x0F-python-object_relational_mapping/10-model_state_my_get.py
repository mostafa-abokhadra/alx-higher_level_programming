#!/usr/bin/python3
"""print object acc to name
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def alchemist():
    flag = 0
    id = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).all()
    for obj in res:
        if obj.name == argv[4]:
            flag = 1
            id = obj.id
            break
    if (flag):
        print(id)
    else:
        print("Not found")


if __name__ == '__main__':
    alchemist()
