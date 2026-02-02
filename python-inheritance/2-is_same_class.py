#!/usr/bin/python3
"""defines a function that checks if an object is exactly an instance of class.
"""


def is_same_class(obj, a_classs):
    """Return True if obj is eactly an instance of a_classs."""
    return type(obj) is a_classs
