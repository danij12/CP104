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
from functions import  list_factors
num = int(input('Enter a positive number: '))
num_list = list_factors(num)
print(f'{num_list}')