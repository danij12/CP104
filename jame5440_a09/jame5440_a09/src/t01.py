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
from functions import file_head

file = input('Enter a filename: ')
linecount = int(input('Enter a number: '))

fh = open(file, 'r', encoding='utf-8')

file_head(fh, linecount)

fh.close()