#!/usr/bin/python3
# lists all cities from the database hbtn_0e_4_usa w/user input of state

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities JOIN states\
        ON cities.state_id=states.id WHERE states.name=%s\
        ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(cities[0] for cities in query_rows))
    cur.close
    db.close
