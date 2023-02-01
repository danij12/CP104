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
from functions import common_ending
string1 = input('Enter a word: ')
string2 = input('Enter a second word: ')
common = common_ending(string1, string2)
print(f"common_ending('{string1}', '{string2}')")
print(f"'{common}'")