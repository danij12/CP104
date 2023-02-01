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
from functions import add_spaces
string = input('Enter a sentence with no spaces: ')
new_string = add_spaces(string)
print(f"add_spaces('{new_string}')")