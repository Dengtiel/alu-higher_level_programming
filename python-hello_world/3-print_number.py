#!/usr/bin/python3
number = 98

try:
    
    print(f"{number} Battery street")
except ValueError:
    print(f"ValueError: Unknown format code 'd' for object of type '{type(number).__name__}'")
