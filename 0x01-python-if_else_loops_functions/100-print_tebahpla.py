#!/usr/bin/python3
wee = ""
for i in range(122, 96, -1):
        if i % 2 == 0:
                wee += chr(i)
        else:
                wee += chr(i - 32)
print("{}".format(wee), end="")
