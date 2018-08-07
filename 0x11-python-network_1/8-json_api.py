#!/usr/bin/python3
'''
    script that takes in letter and send POST req
    to URL with letter as parameter
'''

import requests
from sys import argv

try:
    arg = argv[1]
except IndexError:
    arg = ""

try:
    payload = {'q': arg}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    new_dict = r.json()
    print("[{}] {}".format(new_dict['id'], new_dict['name']))
except KeyError:
    print("No result")
except:
    print("Not a valid JSON")
