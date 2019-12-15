#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id ASC;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
