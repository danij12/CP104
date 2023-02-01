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
#Functions
from functions import multiply_fractions
num1 = int(input('Numerator 1: '))
denom1 = int(input('Denominator 1: '))
num2 = int(input('Numerator 2: '))
denom2 = int(input('Denominator 2: '))
product = multiply_fractions(num1, denom1, num2, denom2)

print(f'Result: {product[0]}/{product[1]} = {product[2]}')