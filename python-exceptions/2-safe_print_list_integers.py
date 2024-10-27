#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        # Try to print the integer; if it fails, it will raise an exception
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue  # Ignore non-integer values
    print("")  # Move to the next line after printing
    return count
