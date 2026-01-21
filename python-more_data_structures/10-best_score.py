#!/usr/bin/python3
def best_score(a_dictionary):
    """Finds the key with the highest value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to search.

    Returns:
        The key with the highest value.
        If the dictionary is empty, returns None.
    """
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
    # Alternatively, we can use the following approach:
    # best_key = None
    # highest_value = float('-inf')
    # for key, value in a_dictionary.items():
    #     if value > highest_value:
    #         highest_value = value
    #         best_key = key
    # return best_key
    # Both methods will yield the same result.
