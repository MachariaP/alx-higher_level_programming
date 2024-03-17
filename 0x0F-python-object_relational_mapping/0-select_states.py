#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def main():
    """
    Main function to access the database and retrieve the states.
    """
    # Establish a connection to the database
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    db_cursor = db_connect.cursor()

    # Execute SQL query to select all states
    db_cursor.execute("SELECT * FROM states")

    # Fetch all rows selected by the query
    rows_selected = db_cursor.fetchall()

    # Print each row
    for row in rows_selected:
        print(row)


if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
