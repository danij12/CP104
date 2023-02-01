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
from functions import time_values
seconds = int(input('Number of seconds: '))
conversion = time_values(seconds)
print(f'{seconds} seconds is the same as: ')
print(f'{conversion[0]} days')
print(f'{conversion[1]} hours')
print( f'{conversion[2]} minutes')