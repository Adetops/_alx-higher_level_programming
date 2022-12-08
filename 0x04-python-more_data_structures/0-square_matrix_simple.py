#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = [[col*col for col in row] for row in matrix]
    return my_matrix
