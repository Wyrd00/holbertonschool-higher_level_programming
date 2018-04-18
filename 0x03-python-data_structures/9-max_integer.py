#!/usr/bin/python3
def max_integer(my_list=[]):
        max_v = 0
        if len(my_list) == 0:
                return None
        for i in my_list:
                if max_v < i:
                        max_v = i
        return max_v
