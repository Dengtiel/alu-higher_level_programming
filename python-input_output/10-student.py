#!/usr/bin/python3
class Student:
    """Class to define a student with first_name, last_name, and age."""


    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first_name, last_name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance, optionally filtering 
        by attributes in the attrs list.

        If attrs is provided, only the attributes that appear in the list will be included 
        in the returned dictionary. Otherwise, all attributes of the Student instance will 
        be included.

        Args:
            attrs (list, optional): A list of attribute names to include in the dictionary.

        Returns:
            dict: The dictionary representation of the student, with the specified attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}

