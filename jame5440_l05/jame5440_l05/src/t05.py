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
from functions import is_leap
year = int(input('Enter a year (>0): '))
leap_year = is_leap(year)
if leap_year == False:
    print(f'{year} is not a leap year')
elif True:
    print(f'{year} is a leap year')