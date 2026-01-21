#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key from a dictionary if it exists.

    Args:
        a_dictionary (dict): The dictionary to modify.
        key: The key to delete from the dictionary.

    Returns:
        The modified dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
    # Alternatively, we can use:
    # a_dictionary.pop(key, None)
    # return a_dictionary
    # Both methods will yield the same result.
