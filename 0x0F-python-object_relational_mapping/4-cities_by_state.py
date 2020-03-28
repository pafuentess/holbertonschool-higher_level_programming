#!/usr/bin/python3

""" conect to database and filter for N """

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) == 4:
        db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], port=3306,
                             host='localhost', db=sys.argv[3])

        cur = db.cursor()
        instruction = ("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON\
                states.id = cities.state_id ORDER BY cities.id")
        cur.execute(instruction)
        rows = cur.fetchall()
        for row in rows:
            print(row)
