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
from functions import list_indexes,list_positives
number = list_positives()
values = number 
print()
target = int(input('Enter a value to look for: '))
locations = list_indexes(values, target)
print(f'{locations}')