#!/usr/bin/python3

""" sts all State objects from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base
from model_state import State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()
        request = session.query(State, City).\
            join(City, State.id == City.state_id).order_by(City.id)
        for state, city in request:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
