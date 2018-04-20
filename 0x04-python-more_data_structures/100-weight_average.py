#!/usr/bin/python3
def weight_average(my_list=[]):
        if my_list:
                total_weighted, total_tup = 0, 0
                for tup in my_list:
                        (num, weighted) = tup
                        total_weighted += weighted
                        total_tup += (num * weighted)
                print("{}: {}".format(total_weighted, total_tup))
                return total_tup/total_weighted
        return 0
