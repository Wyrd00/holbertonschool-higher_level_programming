#!/bin/bash
# Sends POST  request to URL and display body of response
curl -sX POST $1 -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
