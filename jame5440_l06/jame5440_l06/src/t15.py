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
from functions import statistics 
#Variables
n = int(input('Enter number of values: '))
values = statistics(n)
print(f'Minimum: {values[0]}')
print(f'Maximum: {values[1]}')
print(f'Total: {values[2]}')
print(f'Average: {values[3]}')
