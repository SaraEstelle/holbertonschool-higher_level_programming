#!/usr/bin/python3
"""
Defines a function that checks if an object
is an instance of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """Return True if th object is an insrance of a_class or its subclass."""
    return isinstance(obj, a_class)
