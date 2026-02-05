#!/usr/bin/python3
"""
Defines a BaseGeometry class that extends 6-base_geometry.
"""

# Import the BaseGeometry class from 6-base_geometry.py
BaseGeometry = __import__('6-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometry):
    """Extends BaseGeometry with integer validation."""

    def integer_validator(self, name, value):
        """Validate that 'value' is an integer greater than 0.

        Args:
            name (str): name to use in the error message
            value (int): value to validate

        Raises:
            TypeError: if value is not an int
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
