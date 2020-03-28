#!/usr/bin/python3

""" conect to database and filter for N """

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 4:
        db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], port=3306,
                             host='localhost', db=sys.argv[3])

        cur = db.cursor()
        cur.execute('SELECT * FROM states WHERE name like "N%" ORDER BY id ASC')
        rows = cur.fetchall()
        for row in rows:
            print(row)
