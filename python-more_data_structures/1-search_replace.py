#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Searches for an element in a list and replaces it with another element.

    Args:
        my_list (list): The list to search through.
        search: The element to search for.
        replace: The element to replace the searched element with.

    Returns:
        A new list with the searched elements replaced.
    """
    return [replace if element == search else element for element in my_list]
