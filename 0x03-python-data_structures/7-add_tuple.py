#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        alist = list(tuple_a)
        blist = list(tuple_b)

        for i in range(2):
                alist.append(0)
        for j in range(2):
                blist.append(0)
        sum1 = alist[0] + blist[0]
        sum2 = alist[1] + blist[1]
        return (sum1, sum2)
