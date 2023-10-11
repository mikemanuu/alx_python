#!/usr/bin/python3
""" Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
import sys


def search_states(mysql_user, mysql_password, db_name, state_name):
    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(
            user=mysql_user,
            passwd=mysql_password,
            host='localhost',
            port=3306,
            db=db_name
        )

        # Create a cursor
        cursor = conn.cursor()

        # Prepare and execute the SQL query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cursor.execute(query, (state_name,))

        # Fetch all the matching rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python script.py <mysql_user> <mysql_password> <db_name> <state_name>")
    else:
        mysql_user, mysql_password, db_name, state_name = sys.argv[1:5]
        search_states(mysql_user, mysql_password, db_name, state_name)
