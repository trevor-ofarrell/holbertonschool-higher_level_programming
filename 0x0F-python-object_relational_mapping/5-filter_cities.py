#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    l = []
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT cities.name FROM
    cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY cities.id ASC"""
    cur.execute(query, (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        l.append(row[0])
    print(', '.join(l))
    cur.close()
    db.close()
