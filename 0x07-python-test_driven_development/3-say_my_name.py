#!/usr/bin/python3

"""

    Module with one method: say_my_name(first_name, last_name)

"""


def say_my_name(first_name, last_name=""):
    """
    Print first_name and last_name. If not strings, raise TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
