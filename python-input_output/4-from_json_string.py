#!/usr/bin/python3
"""
This module provides a function to parse a JSON\
        string into a Python object.
"""


import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented\
                by the JSON string.
    """
    return json.loads(my_str)
