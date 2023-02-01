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
from functions import scalar_multiply,generate_matrix_num

matrix = generate_matrix_num(2,3,0,100,'int')


print(f'Matrix before scalar multiplication: {matrix} ')

num = int(input('Enter number: '))
scalar_multiply(matrix, num)

print(f'Matrix (with scalar multiplication: {matrix}')