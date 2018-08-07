#!/usr/bin/python3
'''
    takes Github credentials and uses the
    Github API to display id
'''

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

payload = {'username': argv[1], 'password': argv[2]}
r = requests.get(
    "https://api.github.com/users/{}".format(argv[1]),
    auth=HTTPBasicAuth(argv[1],
                       argv[2]))
print(r.json().get("id"))
