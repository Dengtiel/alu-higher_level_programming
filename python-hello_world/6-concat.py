#!/usr/bin/python3
import os
str1 = "Welcome to"
str2 = "Battery Street" if os.getenv('SCHOOL') == 'Battery' else "Holberton School"
print(f"{str1} {str2}!")
