#!/usr/bin/python3
"""listing all state objects
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from model_state import Base, State
import sys


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
results = session.query(State).all()

for data in results:
    print(data.id, ": ", data.name)
