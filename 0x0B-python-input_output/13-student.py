#!/usr/bin/python3
"""

Module with class Student

"""
class_to_json = __import__('10-class_to_json').class_to_json


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
            return class_to_json(self)
        a_dict = {}
        for stuff in attrs:
            try:
                a_dict[stuff] = self.__dict__[stuff]
            except:
                pass
        return a_dic

    def reload_from_json(self, json):
        """replaces all attribute of student instance from json"""
        for stuff in self.__dict__:
            try:
                self.__dict__[stuff] = json[stuff]
            except:
                pass
