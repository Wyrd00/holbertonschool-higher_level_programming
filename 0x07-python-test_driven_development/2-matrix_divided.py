#!/usr/bin/python3
"""

        This is module with one function: matrix_divided(matrix, div)

"""


def matrix_divided(matrix, div):
    """
    Return new_matrix with all int in matrix divided by parameter div
    """
    new_matrix = []
    if not isinstance(matrix, list) and not all(isinstance(int, list)) \
       and not all(isinstance(float, list)) and matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            new_matrix.append([round(elem / div, 2) for elem in row])
    return new_matrix
