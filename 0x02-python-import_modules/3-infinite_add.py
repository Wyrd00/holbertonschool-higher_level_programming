#!/usr/bin/python3
import sys
#sys.argv[1:] = [int(x) for x in sys.argv[1:]]
#num = sys.argv
#argc = len(sys.argv)
num = 0
total = 0
for i in range(1, len(sys.argv)):
        num = int(sys.argv[i])
        total += num
print(total)
