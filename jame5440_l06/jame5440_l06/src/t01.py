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
from functions import sum_even
num = int(input('Enter a number: '))
sum = sum_even(num)
print(f'The sum of all even numbers from 2 to {num} is: {sum}')
