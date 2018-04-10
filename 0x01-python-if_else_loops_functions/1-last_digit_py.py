#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
        nummod = number % -10
else:
        nummod = number % 10
if nummod > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, nummod))
if nummod < 6 and nummod != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, nummod))
if nummod == 0:
        print("Last digit of {} is {} and is 0".format(number, 0))
