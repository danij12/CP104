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
from functions import generate_matrix_char
rows = int(input('Number of rows: '))
cols = int(input('Number of columns: '))
matrix = generate_matrix_char(rows, cols)
print()
print(f'Matrix of characters: ')
print()
print(f'{matrix}')