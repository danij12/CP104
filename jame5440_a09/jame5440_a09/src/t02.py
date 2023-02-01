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
from functions import file_integers

fh = open('numbers.txt', 'r', encoding='utf-8')

numbers = file_integers(fh)

fh.close()

print(f'Numbers: {numbers}')