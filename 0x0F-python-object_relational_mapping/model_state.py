#!/usr/bin/python3
"""class definition of a State and
an instance Base = declarative_base():"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

Base = declarative_base()


class State(Base):
    """class for states in the US"""
    __tablename__ = 'states'
    db = MySQLdb.connect(host='localhost', port=3306,
                         passwd='root', user='root')
    cursor = db.cursor()
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
