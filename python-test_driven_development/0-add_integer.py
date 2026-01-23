#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It accepts integers and floats.
Floats are cast to integers before addition.
Invalid types raise a TypeError.
"""

import math


def add_integer(a, b=98):
    """Add two integers.

    Floats are cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise TypeError("a must be an integer")

    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
