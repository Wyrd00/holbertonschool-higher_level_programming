#!/usr/bin/python3
'''
    send POST request to URl w/email as parameter
    and display body of response
'''

import requests
from sys import argv

payload = {'email': argv[2]}
r = requests.post(argv[1], data=payload)
print(r.text)
