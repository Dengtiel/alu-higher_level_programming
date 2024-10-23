#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    """Prints all integers of a list in reverse order, one per line."""
    if my_list is None:
        my_list = []  # Default to an empty list if None is passed

    for num in reversed(my_list):
        print("{:d}".format(num))
