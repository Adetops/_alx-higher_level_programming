#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[col[i]**2 for i in range(3)] for col in matrix]
