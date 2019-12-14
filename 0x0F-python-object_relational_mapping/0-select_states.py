#!/usr/bin/python3
import MySQLdb
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sys import argv
Base = declarative_base()
Session = sessionmaker()
enginestr = argv[1] + ':' + argv[2] + '@' + 'localhost' + ':'
engine = sqlalchemy.create_engine("{}{}/{}".format(enginestr, 3306, argv[3]))
Session.configure(bind=engine)
session = Session()
for instance in session.query(state).order_by(states.id):
    print(instance.name)
