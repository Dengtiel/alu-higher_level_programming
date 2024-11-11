#!/usr/bin/python3
"""
This module provides a function to write a Python\
        object to a text file in JSON format.
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj: The Python object to be serialized.
        filename (str): The name of the file where the\
                JSON data will be written.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
