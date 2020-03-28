import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], port=3306,
                             host='localhost', db=sys.argv[3])
cursor = db.cursor()
cursor.execute(
    "SELECT id, name FROM states ORDER BY id;")
rows = cursor.fetchal()
for r in rows:
        print(r)
db.close()
