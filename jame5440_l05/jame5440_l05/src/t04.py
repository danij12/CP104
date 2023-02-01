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
#4, 5, 10, 13, 15
#Imports
from functions import closest

target = float(input('Enter a target: '))
v1 = float(input('Enter v1: '))
v2 = float(input('Enter v2: '))
closest = closest(target,v1,v2)

print(f'Closest value to {target} is {closest}')
