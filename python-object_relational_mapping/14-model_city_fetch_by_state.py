#!/usr/bin/python3
"""Affiche toutes les villes avec le nom de l'état associé"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Connexion à la base MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête : join City avec State et tri par City.id
    cities = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()

    # Affichage
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
