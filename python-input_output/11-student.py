#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and reloading."""


class Student:
    """Class that defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the student."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
        return dict(self.__dict__)

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with the given dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
