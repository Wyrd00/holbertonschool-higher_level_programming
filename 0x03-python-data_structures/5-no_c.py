#!/usr/bin/python3
def no_c(my_string):
        for i in my_string:
                if i == 'C' or i == 'c':
                        continue
                else:
                        print("{}".format(i), end="")
