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
from functions import generate_integer_list

n = int(input('Number of values: '))
low = int(input('Low value: '))
high = int(input('High value: '))
print()
print('Values: ',generate_integer_list(n,low,high))