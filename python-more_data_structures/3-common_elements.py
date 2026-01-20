#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Finds common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        A new set containing the common elements between set_1 and set_2.
    """
    return set_1 & set_2
    # Alternatively, we can use:
    # return set_1.intersection(set_2)
    # Both methods will yield the same result.
