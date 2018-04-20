#!/usr/bin/python3
def weight_average(my_list=[]):
        if my_list:
                multiplied, add_num, divisor = 1, 0, 0
                for tup in my_list:
                        for elem in tup:
                                multiplied *= elem
                                if elem == tup[-1]:
                                        divisor += elem
                        add_num += multiplied
                        multiplied = 1
        return add_num / divisor
