#!/usr/bin/python3
"""
lists all City objects from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, cities in session.query(State, City)\
            .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
    session.close()
