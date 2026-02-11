#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and filtering."""


class Student:
    """Class that defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes in this list are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary of the student's attributes.
        """
        result = {}
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        # Return a copy of all attributes, not self.__dict__ directly
        return dict(self.__dict__)
