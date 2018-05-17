#!/usr/bin/python3
"""

Module with one function: load_from_json_file

"""
import json


def load_from_json_file(filename):
    """creates object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
