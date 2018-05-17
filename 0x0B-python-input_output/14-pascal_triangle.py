#!/usr/bin/python3
"""

Module with one function: pascal_triangle

"""


def pascal_triangle(n):
    """creates pascal triangle based on n rows inputed"""
    result = []
    for row in range(n):
        row = [1]
        if result:
            prev_row = result[-1]
            for nums in zip(prev_row, prev_row[1:]):
                row.extend([sum(nums)])
            row.append(1)
        result.append(row)
    return result
