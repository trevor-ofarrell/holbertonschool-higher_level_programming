#!/usr/bin/python3
def matrix_divided(matrix, div):

    """divide a 3x2 matrix by 2"""

    if isinstance(matrix[0], list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if isinstance(matrix[1], list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for elements in matrix[0]:
        if isinstance(elements, (int, float)) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for elements in matrix[1]:
        if isinstance(elements, (int, float)) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, int) is False:
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    return [[round(y / div, 2) for y in x] for x in matrix]
