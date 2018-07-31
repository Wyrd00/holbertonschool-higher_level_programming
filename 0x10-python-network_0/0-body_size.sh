#!/bin/bash
# Sends request to URL and display body size of response

curl -Is $1 | grep -i "Content-Length:" | cut -d " " -f2
