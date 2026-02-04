#!/usr/bin/python3
"""
Defines the BaseGeometry class, extending 6-base_geometry with integer validation.
"""

# Import BaseGeometry from 6-base_geometry
BaseGeometry6 = __import__('6-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometry6):
    """BaseGeometry: provides base geometry utilities with integer validation."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that 'value' is an integer greater than 0.

        Args:
            name (str): name to use in the error message
            value (int): value to validate

        Raises:
            TypeError: if value is not an int
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
