#!/usr/bin/python3

""" sts all State objects from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()
        request = session.query(State).filter(State.name.like(
                                              '%a%')).order_by(State.id)
        for i in request:
            print("{}: {}".format(i.id, i.name))
