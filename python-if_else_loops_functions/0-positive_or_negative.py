#!/usr/bin/python3
import random

# This line generates a random integer between -10 and 10
number = random.randint(-10, 10)

# Your code goes here. Please remove the comment before the following code.
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
