#!/usr/bin/python3
"""
Main file - rotate_2d_matrix(matrix)
"""


def rotate_2d_matrix(matrix):
    """
    function an n x n 2D matrix,
    rotate it 90 degrees clockwise.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
