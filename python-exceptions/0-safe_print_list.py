#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # To count the number of elements printed
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1  # Increment count for each successfully printed element
    except IndexError:
        pass  # Ignore IndexError if x is greater than the list length
    print("")  # Print new line after all elements
    return count  # Return the actual number of elements printed

