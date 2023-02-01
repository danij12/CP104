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
from functions import pollution_level
num = int(input('Enter a number: '))
level =pollution_level(num)
print(f'pollution_level({num}) -> "{level}"')