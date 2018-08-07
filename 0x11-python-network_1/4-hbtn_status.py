#!/usr/bin/python3
'''
    fetches status with package requests
'''

import requests

r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t type: {}".format(type(r.text)))
print("\t content: {}".format(r.text))
