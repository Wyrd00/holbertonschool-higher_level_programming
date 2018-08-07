#!/usr/bin/python3
'''
    send request to URL and display value of variable
    X-Request-Id in response header
'''
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('x-request-id'))

