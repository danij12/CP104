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
from functions import text_analyze

txt = input('Enter a string: ')
uppr = text_analyze(txt)[0]
lowr =  text_analyze(txt)[1]
dgts =  text_analyze(txt)[2]
whtspc =  text_analyze(txt)[3]
print()
print(f'upper case letters: {uppr}')
print(f'lower case letters: {lowr}')
print(f'digits: {dgts}')
print(f'whitespace characters: {whtspc}')
