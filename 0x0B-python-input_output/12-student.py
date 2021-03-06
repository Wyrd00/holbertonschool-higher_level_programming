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

    def to_json(self, attrs=None):
        """return dict representation of Student instance"""
        if attrs is None:
            return self.__dict__
        a_dict = {}
        for stuff in attrs:
            try:
                a_dict[stuff] = self.__dict__[stuff]
            except:
                pass
        return a_dict
