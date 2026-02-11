#!/usr/bin/python3
"""Module that defines a function to convert an object to JSON."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj: The object to convert.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
