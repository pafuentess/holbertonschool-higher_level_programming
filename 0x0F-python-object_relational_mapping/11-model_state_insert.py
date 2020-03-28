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
        state_name = State(name='Louisiana')
        session.add(state_name)
        session.commit()
        print(state_name.id)
