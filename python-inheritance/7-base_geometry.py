#!/usr/bin/python3
"""
This module defines a BaseGeometry class with area and integer validation methods.
"""


class BaseGeometry:
    """
    A base class for geometry with basic area and integer validation methods.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        
        :raises Exception: Always raises Exception with a specific message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        
        :param name: The name of the parameter (expected to be a string)
        :param value: The value to validate
        :raises TypeError: If value is not an integer
        :raises ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

