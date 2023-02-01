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
from functions import symmetric_difference,generate_integer_list
n = int(input('Number of values: '))
low = int(input('Low value: '))
high = int(input('High value: '))
values1 = generate_integer_list(n, low, high)
print()
n = int(input('Number of values: '))
low = int(input('Low value: '))
high = int(input('High value: '))
values2 = generate_integer_list(n, low, high)
print()
target = symmetric_difference(values1, values2)

print(f'Values 1: {values1}')
print(f'Values 2: {values2}')
print()
print(f'Difference: {target}')