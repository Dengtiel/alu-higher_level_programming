#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    """
    a_dictionary[key] = value  # Update the value for the given key
    return a_dictionary  # Return the updated dictionary
