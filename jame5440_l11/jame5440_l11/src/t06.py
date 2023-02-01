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
from functions import stats,generate_matrix_num
rows = int(input('Number of rows: '))
cols = int(input('Number of columns: '))
low = int(input('Low value: '))
high = int(input('High value: '))
matrix = generate_matrix_num(rows, cols, low, high, 'int')
smallest,largest,total,average = stats(matrix)
print()
print(f'{matrix}')
print(f'Smallest = {smallest}')
print(f'Largest = {largest}')
print(f'Total = {total}')
print(f'Average = {average}')


