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
from functions import list_categorize,generate_integer_list
n = int(input('Number of values: '))
low = int(input('Low value: '))
high = int(input('High value: '))
values = generate_integer_list(n, low, high)
print()
ans = list_categorize(values)
print(f'Values: {values}')
print()
print(f'Negatives: {ans[0]}')
print(f'Positives: {ans[1]}')
print(f'Zeroes: {ans[2]}')
print(f'Evens: {ans[3]}')
print(f'Odds: {ans[4]}')

