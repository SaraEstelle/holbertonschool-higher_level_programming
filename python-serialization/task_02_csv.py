# task_02_csv.py
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en fichier JSON nommé 'data.json'.

    Paramètre:
    - csv_filename: str, nom du fichier CSV à lire

    Retourne:
    - True si conversion réussie, False sinon
    """
    try:
        # Lire le fichier CSV et convertir chaque ligne en dictionnaire
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)  # Liste de dictionnaires

        # Sérialiser la liste en JSON et écrire dans 'data.json'
        with open('data.json', 'w') as jsonfile:
            json.dump(rows, jsonfile, indent=4)  # indent=4 pour lisibilité

        return True

    except FileNotFoundError:
        print(f"Erreur : le fichier {csv_filename} n'existe pas.")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return False
