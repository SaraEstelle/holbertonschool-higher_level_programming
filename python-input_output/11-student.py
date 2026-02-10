#!/usr/bin/python3
class Student:
    """Class thatt defines a Student."""


    def __init__(self, fisrt_name, last_name, age):
        self.first_name = fisrt_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a student instance."""
        if isinstance(attrs, list) and all(isinstance (x, str)for x in attrs):
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key,value)
