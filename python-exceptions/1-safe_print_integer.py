#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer value safely.

    Args:
        value: The value to print.

    Returns:
        bool: True if the value was printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
