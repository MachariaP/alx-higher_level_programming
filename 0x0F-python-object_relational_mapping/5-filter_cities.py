#!/usr/bin/python3
"""
This script takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    # Connect to the MySQL database
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    with db_connect.cursor() as db_cursor:
        # Execute SQL query to retrieve cities of the specified state
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        # Fetch all selected rows
        rows_selected = db_cursor.fetchall()

    # Print the names of cities if any rows are selected
    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
