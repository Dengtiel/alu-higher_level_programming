#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if not my_list:  # Check if the list is empty
        return None

    max_value = my_list[0]  # Initialize max_value with the first element
    for num in my_list:  # Iterate through the list
        if num > max_value:  # Update max_value if a larger number is found
            max_value = num

    return max_value  # Return the largest number found
