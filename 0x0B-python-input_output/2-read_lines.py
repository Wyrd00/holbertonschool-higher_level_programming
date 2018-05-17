#!/usr/bin/python3
"""

Module w/one function: read_lines

"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and print to STDOUT"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        for i in range(nb_lines):
            print(f.readline(), end="")
