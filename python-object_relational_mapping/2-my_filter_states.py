#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Create SQL query using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(state_name)

    # Execute query
    cursor.execute(query)

    # Fetch results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
