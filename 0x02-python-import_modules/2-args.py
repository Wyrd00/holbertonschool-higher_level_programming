#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
print("{} ".format(argc), end="")
if argc == 0:
        print("arguments.")
elif argc == 1:
        print("argument:")
        print("{}: {}".format(1, sys.argv[1]))
else:
        print(":")
        for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))
