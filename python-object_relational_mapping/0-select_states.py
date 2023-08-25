#!/usr/bin/python3

'''Lists all states from the database hbtn_0e_0_usa.'''

import MySQLdb
from sys import argv

if __name__ == '__main__':

    if len(argv) != 4:
        print('Usage: {} <username> <password> <database>'.format(argv[0]))

        argv.exit

    username = argv[1]
    password = argv[2]
    database = argv[3]

    try:
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDEY BY id ASC")

    for row in cursor.fetchall():
        print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print('Error connecting to MySQL:', e)
        argv.exit(1)
