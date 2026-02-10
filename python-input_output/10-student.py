#!/usr/bin/python3
class Student:
    """Class that Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of Student instance."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
        return self.__dict__
