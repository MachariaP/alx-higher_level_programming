#!/usr/bin/python3
"""
This script retrieves and displays all values in the states
where `name` matches the argument provided by the user
from the database `hbtn_0e_0_usa`.
This version of the script is protected against MySQL injections.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    db_connect = db.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Create a cursor object to execute SQL queries
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s "
        "ORDER BY states.id ASC",
        {'name': argv[4]}
    )

    # Fetch all selected rows
    rows_selected = db_cursor.fetchall()

    # Print the selected rows
    for row in rows_selected:
        print(row)
