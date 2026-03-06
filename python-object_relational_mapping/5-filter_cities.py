#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve arguments
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

    # SQL query (safe from SQL injection)
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute query
    cursor.execute(query, (state_name,))

    # Fetch results
    rows = cursor.fetchall()

    # Extract city names
    cities = [row[0] for row in rows]

    # Print cities separated by comma
    print(", ".join(cities))

    # Close connection
    cursor.close()
    db.close()
