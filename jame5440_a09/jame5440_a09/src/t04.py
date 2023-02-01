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
from functions import flatten

matrix = [[10, 20, 11], [9, 0, 5], [19, 2, 22]]
print(f'Original Matrix: {matrix}')
flat = flatten(matrix)
print(f'Flattened Matrix: {flat}')