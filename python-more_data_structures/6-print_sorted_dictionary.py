#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

# You can use either:
# for key in sorted(a_dictionary):
# print("{}: {}".format(key, a_dictionary[key]))
# or
# for key in sorted(a_dictionary.keys()):
# print("{}: {}".format(key, a_dictionary[key]))
# Both methods sort the dictionary keys and produce the same result.
# The choice between them is mostly a matter
# of style or preference.
# Sorting the keys ensures a consistent
# and predictable output, which improves
# readability and debugging, especially
# when the dictionary is created dynamically
# or when the order of keys matters.

# Even though Python 3.7+ preserves insertion order
# in dictionaries, explicitly
# sorting the keys guarantees a stable order for presentation.

# This function is useful for displaying
# dictionary contents in a clean and
# organized way. It works with any
# dictionary whose keys are sortable and can be
# reused in many programming situations
# where sorted output is needed.
