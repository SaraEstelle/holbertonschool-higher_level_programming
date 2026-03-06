#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This version is safe from SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Safe SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    # Execute query with parameter
    cursor.execute(query, (state_name,))

    # Fetch results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
