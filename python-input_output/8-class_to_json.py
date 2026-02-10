#!/usr/bin/python3
def class_to_json(obj):

    """Returns the dictionary description for json serialization of an object."""
    return obj.__dict__
