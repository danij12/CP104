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
from functions import c_to_f
celsius = int(input('Enter a temperature (c):' ))
fahrenheit = c_to_f(celsius)
print(f'{celsius} C = {fahrenheit} F')
