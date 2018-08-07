#!/usr/bin/python3
'''
    script that takes URL, send request to URL, and
    displays value of X-Request-Id in header
'''

import urllib.request
import sys

if __name__ == '__main__':
    arg = sys.argv[1]
    with urllib.request.urlopen(arg) as resp:
        print(resp.headers.get("X-Request-Id"))
