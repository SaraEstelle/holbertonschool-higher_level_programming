#!/usr/bin/python3
"""defines a function that checks if an object
is an instance of a subclass of a given class.
"""


def inherits_from(obj, a_class):
    """Return True if the object
    is an instance of a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
