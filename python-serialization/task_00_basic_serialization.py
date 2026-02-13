# task_00_basic_serialization.py
import json  # Importation du module json pour la sérialisation et désérialisation

def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.

    Paramètres:
    - data: dict, le dictionnaire à sérialiser
    - filename: str, le nom du fichier de sortie
    """
    # Ouvre le fichier en mode écriture ('w'), remplace le fichier s'il existe
    with open(filename, 'w') as file:
        # Écrit le dictionnaire dans le fichier au format JSON
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et le convertit en dictionnaire Python.

    Paramètres:
    - filename: str, le nom du fichier JSON à lire

    Retourne:
    - dict: le dictionnaire recréé à partir du fichier JSON
    """
    # Ouvre le fichier en mode lecture ('r')
    with open(filename, 'r') as file:
        # Lit les données JSON et les convertit en dictionnaire Python
        data = json.load(file)
    # Retourne le dictionnaire recréé
    return data
