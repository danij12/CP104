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
from functions import generate_matrix_num
rows = int(input('Number of rows: '))
cols = int(input('Number of columns: '))
low = int(input('Low value: '))
high = int(input('High value: '))
value_type = input('Type of values: ')
matrix = generate_matrix_num(rows, cols, low, high, value_type)
print(f'{matrix}')