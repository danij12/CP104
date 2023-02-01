"""
-------------------------------------------------------
Lab/Assignment  Testing
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
Version: 2021-10-08
-------------------------------------------------------
"""
from functions import matrix_equal,generate_matrix_char
matrix1 = generate_matrix_char(2,3)
matrix2 = generate_matrix_char(2,3)



equal = matrix_equal(matrix1, matrix2)
print(f'First matrix')
print(f'Matrix 1: {matrix1}')
print(f'Second matrix: ')
print(f'Matrix 2: {matrix2}')
print()
print(f'Equal matricies: {equal}')
