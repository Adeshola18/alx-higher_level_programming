#!/usr/bin/env python3
"""
a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.id)
    for r in res:
        print("{}: {}".format(r.id, r.name))
        for c in r.cities:
            print("\t{}: {}".format(c.id, c.name))