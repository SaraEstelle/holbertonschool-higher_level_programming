# task_01_pickle.py
import pickle  # Import du module pickle pour sérialisation binaire

class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialise l'objet avec ses attributs."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'objet courant et le sauvegarde dans un fichier."""
        try:
            with open(filename, 'wb') as file:  # wb = write binary
                pickle.dump(self, file)         # Sérialisation de self
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge un fichier et retourne une instance de CustomObject."""
        try:
            with open(filename, 'rb') as file:  # rb = read binary
                obj = pickle.load(file)         # Désérialisation
            return obj
        except Exception as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None
