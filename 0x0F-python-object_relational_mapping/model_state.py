#!/usr/bin/python3
"""k"""
import sqlite3
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
