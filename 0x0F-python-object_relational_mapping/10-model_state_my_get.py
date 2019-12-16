#!/usr/bin/python3
"""script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa"""

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
            State.name == argv[4]).order_by(State.id):
        if instance:
            print("{}".format(instance.id))
        else:
            print("Not found")
