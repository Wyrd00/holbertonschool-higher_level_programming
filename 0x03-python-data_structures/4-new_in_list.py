#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        new_list = []
        for i in range(len(my_list)):
                if idx == i:
                        new_list.append(element)
                else:
                        new_list.append(my_list[i])
        return new_list
