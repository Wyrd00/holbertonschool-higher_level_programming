#!/usr/bin/python3
"""

Module: class MyList inherits from list

"""


class MyList(list):
    """

    """
    def __init__(self):
        """Spec method __init__ that inherits from baseclass __init__"""
        super().__init__()

    def print_sorted(self):
        """Sort the list"""
        print("{}".format(sorted(self)))
