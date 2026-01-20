#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides elements of two lists element-wise up to a specified length.

    Args:
        my_list_1 (list): The first list of numbers.
        my_list_2 (list): The second list of numbers.
        list_length (int): The number of elements to divide.
    Returns:
        list: A new list containing the results of the divisions.
    """
    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            division = 0
        except IndexError:
            division = 0
        except TypeError:
            division = 0
        result.append(division)
    return result
