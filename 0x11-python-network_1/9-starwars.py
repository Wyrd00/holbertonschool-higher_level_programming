#!/usr/bin/python3
'''
    sends search request to Star Wars API
'''

import requests
from sys import argv

r = requests.get("https://swapi.co/api/people/?search=r2",
                 params={'search': argv[1]})
body = r.json()
print("Number of results: {}".format(body.get('count')))
for search in body.get('results'):
    print(search['name'])
