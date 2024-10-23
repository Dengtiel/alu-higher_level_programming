#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list."""

    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy if idx is out of range

    # Create a copy of the original list
    new_list = my_list.copy()
    new_list[idx] = element  # Replace the element at the specified index
    return new_list
