#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            # Check if both lists have elements at index i
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result = 0
            else:
                # Attempt division
                result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            result_list.append(result)
    return result_list
