#!/usr/bin/python3
'''
    script that sends POST req to URL and
    display body of response (decoded in utf8)
'''

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    arg = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')
    with urllib.request.urlopen(arg, data) as resp:
        html = resp.read()
        print(html.decode('utf-8'))
