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
from functions import file_stats

fh = open('addresses.txt', 'r', encoding='utf-8')

ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()

print(f'Number of uppercase letters: {ucount}')
print(f'Number of lowercase letters: {lcount}')
print(f'Number of digits in the file: {dcount}')
print(f'Number of whitespace characters in the file: {wcount}')