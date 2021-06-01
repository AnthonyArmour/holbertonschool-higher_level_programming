#!/usr/bin/python3
"""
lists all states and there cities table
"""
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for item in states:
        for n in range(len(item.cities)):
            print("{}: {} -> {}"
                  .format(item.cities[n].id, item.cities[n].name, item.name))
    session.commit()
