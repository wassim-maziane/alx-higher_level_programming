#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = len(matrix)
    m = len(matrix[0])
    M = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            M[i][j] = matrix[i][j] * matrix[i][j]
    return M
