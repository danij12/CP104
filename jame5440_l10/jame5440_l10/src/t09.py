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
from functions import count_frequency_value
print("file 'numbers.txt' open for reading")
fh = open('numbers.txt','r')
value = int(input('Value to count: '))
count = count_frequency_value(fh, value)
print(f'{value} appears {count} time(s)')