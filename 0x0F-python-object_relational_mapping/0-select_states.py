#!/usr/bin/python3
"""script to list all states in db"""
import MySQLdb
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
if __name__ == "__main__":
    Base = declarative_base()
    Session = sessionmaker()
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states; ORDER BY state.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
