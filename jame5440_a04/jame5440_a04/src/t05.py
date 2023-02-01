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
#Imports
from functions import yee_ha

num = int(input('Enter a number: '))
response = yee_ha(num)
print(f'yee_ha({num}) -> "{response}"')