#!/usr/bin/python3
'''
    Module to find peak of unsorted list of int
'''


def find_peak(list_of_integers):
    #last needs to be entire length, list_of_int[-1] refer to last index
    last = len(list_of_integers)
    mid = int(last / 2)

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[mid]

    try:
        if list_of_integers[mid - 1] <= list_of_integers[mid] and \
                list_of_integers[mid + 1] <= list_of_integers[mid]:
            return list_of_integers[mid]

    except IndexError:
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            return list_of_integers[mid - 1]
        else:
            return list_of_integers[mid]

    if list_of_integers[mid + 1] > list_of_integers[mid - 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return find_peak(list_of_integers[:mid])
