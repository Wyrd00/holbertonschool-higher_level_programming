#!/usr/bin/python3
"""

Module with class Student

"""


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict representation of Student instance"""
        return self.__dict__
