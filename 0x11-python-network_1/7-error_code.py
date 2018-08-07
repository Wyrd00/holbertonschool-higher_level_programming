#!/usr/bin/python3
'''
    request to URL and display body of response
    print error code if applicable
'''

import requests
from sys import argv

if __name__ == '__main__':
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error Code: {}".format(r.status_code))
