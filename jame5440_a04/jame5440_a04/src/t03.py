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
from functions import product_largest
v1 = float(input('Enter a number: '))
v2 = float(input('Enter a second number: '))
v3 = float(input('Enter a third number: '))
product = product_largest(v1,v2,v3)
print(f'product_largest({v1},{v2},{v3}) -> {product}')

