#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of 'search' in 'my_list' with 'replace' in a new list.
    """
    return [replace if item == search else item for item in my_list]
