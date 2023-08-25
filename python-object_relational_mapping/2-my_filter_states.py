#!/usr/bin/python3
""" Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. """

import sys
import MySQLdb

if __name__ == '__main_-':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{:S}' ORDER BY \ id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
