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
from functions import fraction_product
num1 = int(input('Enter number of fraction:'))
den1 = int(input('Enter denominator of fraction 1: '))
num2 = int(input('Enter numerator of fraction 2: '))
den2 = int(input('Enter denominator of fraction 2: '))
product = fraction_product(num1,den1,num2,den2)
print(f'Product = {product[0]}/{product[1]}')
print(f'Decimal = {product[2]}')