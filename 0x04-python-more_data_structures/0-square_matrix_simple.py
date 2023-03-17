#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    
    # Loop through each element in the input matrix and compute its square
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] ** 2
    
    # Return the new matrix
    return result
