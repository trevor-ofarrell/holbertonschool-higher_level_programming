#!/usr/bin/python3
"""script that prints all City objects from
the database hbtn_0e_14_usa"""

from model_state import Base, State
from model_city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sys import argv

if __name__ == "__main__":
    Base = declarative_base()
    Session = sessionmaker()
    enginestr = 'mysql+mysqldb://'
    engine = sqlalchemy.create_engine(
        "{}{}:{}{}/{}".format(enginestr, argv[1], argv[2],
                              '@localhost:3306', argv[3]))
    Session.configure(bind=engine)
    session = Session()
    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
