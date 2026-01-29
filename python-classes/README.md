🐍 Python — Classes and Objects


📑 Table des matières:

📚 Introduction

🎯 Objectifs pédagogiques

📁 Structure du projet

🧠 Concepts clés

🧩 Détails des fichiers

🧪 Tests & Validation

📐 Diagrammes & Modèles

🛠️ Bonnes pratiques

📎 Ressources utiles

✨ Auteur

📚 Introduction

Ce projet introduit les fondations de la programmation orientée objet (POO) en Python.
Il explore la création de classes, la manipulation d’objets, l’encapsulation, les propriétés, les méthodes spéciales, et la logique interne du modèle objet de Python.

L’objectif est de comprendre comment structurer un programme autour d’objets, et comment Python implémente la POO de manière simple, flexible et élégante.

🎯 Objectifs pédagogiques

Comprendre la différence entre classe et instance

Manipuler des attributs privés et publics

Utiliser @property et @setter

Implémenter des méthodes d’instance

Valider des données dans __init__

Utiliser les méthodes spéciales (__str__, __repr__)

Comprendre le namespace d’une classe

Respecter la PEP 8 et les conventions Holberton

📁 Structure du projet

Code
.
├── 0-square.py
├── 1-square.py
├── 2-square.py
├── 3-square.py
├── 4-square.py
├── 5-square.py
├── 6-square.py
├── tests/
│   ├── test_0.txt
│   ├── test_1.txt
│   └── ...
└── README.md

🧠 Concepts clés

🔹 Classe vs Instance
Code
Class  → Plan
Object → Instance du plan
🔹 Le rôle de self
self représente l’instance courante.
Il permet d’accéder aux attributs internes.

🔹 Encapsulation
Python utilise la convention :

Code
self.__attribute  # attribut privé
🔹 Propriétés
Elles permettent un contrôle fin des attributs :

python
@property
def size(self):
    return self.__size

🧩 Détails des fichiers
Fichier	Description
0-square.py	Classe vide
1-square.py	Attribut privé
2-square.py	Validation de la taille
3-square.py	Méthode area()
4-square.py	Propriétés (@property)
5-square.py	Représentation d’objet
6-square.py	Position + affichage

🧪 Tests & Validation

✔️ Doctests
Code
python3 -m doctest -v <fichier>
✔️ PEP 8
Code
pycodestyle .
✔️ Exécution
Tous les fichiers doivent commencer par :

Code
#!/usr/bin/python3

📐 Diagrammes & Modèles

🔸 Diagramme conceptuel (POO Python)

Code
        ┌────────────────┐
        │     Class      │
        └───────┬────────┘
                │ blueprint
        ┌───────┴────────┐
        │    Instance     │
        └───────┬────────┘
                │ has
        ┌───────┴────────┐
        │   Attributes    │
        └───────┬────────┘
                │ accessed via self
        ┌───────┴────────┐
        │     Methods     │
        └─────────────────┘
🔸 Cycle de vie d’un objet
Code
Définition → Instanciation → Manipulation → Destruction
🛠️ Bonnes pratiques
Toujours valider les entrées dans __init__ ou les setters

Utiliser des docstrings claires et concises

Préférer les propriétés plutôt que l’accès direct aux attributs

Respecter la PEP 8 pour la lisibilité

Tester chaque méthode individuellement

Garder les classes simples et cohérentes (principe SRP)

📎 Ressources utiles
Documentation Python : https://docs.python.org/3/tutorial/classes.html (docs.python.org in Bing)

PEP 8 : https://peps.python.org/pep-0008/

Tutoriel POO Python : https://realpython.com/python3-object-oriented-programming/ (realpython.com in Bing)

✨ Auteur
Projet réalisé dans le cadre du programme Holberton School.
Rédigé et documenté par Sara Rebati.
