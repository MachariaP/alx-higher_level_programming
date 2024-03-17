#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""


import MySQLdb as db
from sys import argv


"""
Access to the database and get the states
from the database.
"""

if __name__ == '__main__':
    # Establishing a connection to the database
    db_connect = db.connect(host="localhost",
                            port=3306,
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3])

    # Creating a cursor object to execute SQL queries
    db_cursor = db_connect.cursor()

    # Executing SQL query to select states and ordering them
    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")

    # Fetching all selected rows
    rows_selected = db_cursor.fetchall()

    # Printing each selected row
    for row in rows_selected:
        print(row)
