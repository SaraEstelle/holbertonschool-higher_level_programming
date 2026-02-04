#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry: provides base geometry utilities."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that 'value' is an integer greater than 0.

        Args:
            name (str): name to use in the error message.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
