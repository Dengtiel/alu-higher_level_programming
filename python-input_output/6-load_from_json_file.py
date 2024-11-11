#!/usr/bin/python3
"""
This module provides a function to load a Python\
        object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object created from the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
