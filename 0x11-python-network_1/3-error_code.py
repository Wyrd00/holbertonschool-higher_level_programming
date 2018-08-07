#!/usr/bin/python3
'''
    Display body or response decoded in utf-8
    with Error Code
'''

import urllib.request as request
from sys import argv
import urllib.error as Error

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
    except Error.HTTPError as e:
        print("Error code: {}".format(e.code))
