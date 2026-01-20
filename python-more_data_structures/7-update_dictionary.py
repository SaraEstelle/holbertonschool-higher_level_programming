#!/usr/bin/python33
def update_dictionary(a_dictionary, key, value):
    """Updates a dictionary by adding a new key-value pair or updating an existing key's value.

    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to add or update in the dictionary.
        value: The value associated with the key.

    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

    # Alternatively, we can use:
    # a_dictionary.update({key: value})
    # return a_dictionary
    # Both methods will yield the same result.
