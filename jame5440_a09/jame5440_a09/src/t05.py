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
from functions import matrix_rotate_right

matrix = [[3, 4, 0], [8, 12, 3], [0, 0, 0]]
print(f'Original Matrix: {matrix}')
rotated = matrix_rotate_right(matrix)
print(f'Rotated Matrix: {rotated}')