#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiplies all values in a dictionary by 2.

    Args:
        a_dictionary (dict): The dictionary to modify.

    Returns:
        The modified dictionary with values multiplied by 2.
    """
    for key in a_dictionary:
        a_dictionary[key] *= 2
    return a_dictionary
    # Alternatively, we can use dictionary comprehension:
    # return {key: value * 2 for key, value in a_dictionary.items()}
    # Both methods will yield the same result.
