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
from functions import is_valid_isbn
from _ast import Is
isbn = input('Enter ISBN: ')
valid = is_valid_isbn(isbn)
print(f"is_valid_isbn('{isbn}')")
print(f'{valid}')