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
from functions import number_stats
fh = open('numbers.txt','r')
numbers = number_stats(fh)
print(f'Smallest: {numbers[0]}')
print(f'Largest: {numbers[1]}')
print(f'Total: {numbers[2]}')
print(f'Average: {numbers[3]}')