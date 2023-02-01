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
from functions import population_growth
target = int(input('target: '))
current = int(input('current: '))
rate = int(input('rate: '))
years = population_growth(target,current,rate)
print(f'population_growth({target}, {current}, {rate} -> {years})')