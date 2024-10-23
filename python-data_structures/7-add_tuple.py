#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    # Ensure both tuples have at least 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Return a tuple with the sum of the first and second elements
    # of both tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
