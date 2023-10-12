#!/usr/bin/python3
"""
Displays all values
in the states table of
hbtn_0e_0_usa where 
name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM `states` WHERE BINARY `name` = '{}' "
        "ORDER BY id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
