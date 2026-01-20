#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Finds elements that are in only one of the two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.
    Returns:
        A new set containing elements that are in only one of the two sets.
    """
    return set_1 ^ set_2
    # Alternatively, we can use:
    # return set_1.symmetric_difference(set_2)
    # Both methods will yield the same result
