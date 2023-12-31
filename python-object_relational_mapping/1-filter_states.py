#!/usr/bin/python3

""" Importing modules """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
