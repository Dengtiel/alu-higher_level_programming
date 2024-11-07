#!/usr/bin/python3
"""Module to check class inheritance and instances."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an
    instance of, or
    if the object is an instance of a class\
    that inherited
    from, the specified class; otherwise False.
    Args:
        obj: The object to check.\
        a_class: The class to match the 
        object against.

    Returns:
        bool: True if `obj` is an instance\
        of `a_class` or
        an instance of a subclass of\
        `a_class`; otherwise False.
    """
    return isinstance(obj, a_class)
