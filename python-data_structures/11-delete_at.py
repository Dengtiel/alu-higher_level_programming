#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if 0 <= idx < len(my_list):
        del my_list[idx]  # Delete the item at the specified index
    return my_list  # Return the modified list
