#!/usr/bin/python3
"""script to list all states in db that contain the char a"""

from model_state import Base, State
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
    for instance in session.query(State).filter(
            State.name.contains('a')).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
