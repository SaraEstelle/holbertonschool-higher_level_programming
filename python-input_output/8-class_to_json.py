#!/usr/bin/python3
"""Module that defines a function to return the dictionary representation
of a class object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
