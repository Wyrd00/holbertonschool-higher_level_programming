#!/usr/bin/python3
'''
    request to URL and display body of response
    print error code if applicable
'''

import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error Code: {}".format(r.status_code))
