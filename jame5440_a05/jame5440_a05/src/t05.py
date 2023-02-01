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
from functions import range_total
start = int(input('Enter a start value: '))
increment = int(input('Enter a increment: '))
count = int(input('Enter the number of values in the range: '))
ans = range_total(start,increment,count)
print(f'{ans}')
