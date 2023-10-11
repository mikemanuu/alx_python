#!/usr/bin/python3
"""  List all states with a name starting with N (upper N) from the database hbtn_0e_0_usa. """
import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    DBconnection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passw=password,
        database=database_name
    )

    cursor = DBconnection.cursor()

    cursor.execute(
        "SELECT id,name\
        FROM states \
        WHERE BINARY name LIKE 'N%\
        ORDER BY id ASC"
    )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    DBconnection.close()
