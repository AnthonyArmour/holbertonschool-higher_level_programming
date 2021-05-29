#!/usr/bin/python3
"""
lists all states from states table
"""
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
