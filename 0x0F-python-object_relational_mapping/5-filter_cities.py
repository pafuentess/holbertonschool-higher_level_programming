#!/usr/bin/python3

""" conect to database and filter for N """

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) == 5:
        db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], port=3306,
                             host='localhost', db=sys.argv[3])

        cur = db.cursor()
        instruction = "SELECT cities.name FROM cities INNER JOIN states ON\
                states.id = cities.state_id WHERE states.name ='{}'\
                ORDER BY cities.id;".format(sys.argv[4].split('\'')[0])
        cur.execute(instruction)
        rows = cur.fetchall()
        print(", ".join([row[0] for row in rows]))
