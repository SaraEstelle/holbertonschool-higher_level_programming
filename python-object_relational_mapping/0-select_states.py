#!/usr/bin/python3
"""
Script that lists all states from a MySQL database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Prevent code execution when imported
    """

    # récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connexion à la base de données MySQL
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # création du curseur
    cursor = conn.cursor()

    # requête SQL pour récupérer les states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # récupération des résultats
    rows = cursor.fetchall()

    # affichage des résultats
    for row in rows:
        print(row)

    # fermeture du curseur et de la connexion
    cursor.close()
    conn.close()
