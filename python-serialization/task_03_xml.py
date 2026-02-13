# task_03_xml.py
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en fichier XML.

    Paramètres:
    - dictionary: dict à sérialiser
    - filename: nom du fichier XML de sortie
    """
    root = ET.Element("data")  # Création de l'élément racine

    for key, value in dictionary.items():  # Ajout de sous-éléments
        child = ET.SubElement(root, key)
        child.text = str(value)  # Toujours convertir en string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Paramètre:
    - filename: nom du fichier XML à lire

    Retourne:
    - dict contenant les données
    """
    try:
        tree = ET.parse(filename)  # Parse le fichier XML
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}  # Reconstruire dict
        return dictionary
    except FileNotFoundError:
        print(f"Erreur : le fichier {filename} n'existe pas.")
        return None
    except ET.ParseError:
        print(f"Erreur : le fichier {filename} n'est pas un XML valide.")
        return None
