#!/usr/bin/python3
"""Ajoute l’état 'Louisiana' à la base hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Création du nouvel état
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de l'ID généré
    print(new_state.id)

    session.close()
