#!/usr/bin/python3
"""

Module with one function: from_json_string

"""
import json


def save_to_json_file(my_obj, filename):
    """write object to text file using json rep"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
