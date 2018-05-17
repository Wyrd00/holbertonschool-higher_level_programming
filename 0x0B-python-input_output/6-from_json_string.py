#!/usr/bin/python3
"""

Module with one function: to_json_string

"""
import json


def from_json_string(my_str):
    """returns object that was originally json represented"""
    return json.loads(my_str)
