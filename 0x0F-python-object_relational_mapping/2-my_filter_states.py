#!/usr/bin/python3
"""script that lists all states with a name
matching user input from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    query1 = "SELECT * FROM states WHERE name LIKE BINARY"
    query2 = "ORDER BY states.id ASC;"
    query = "{} '%{}%' {}".format(query1, argv[4], query2)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
