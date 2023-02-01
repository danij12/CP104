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
#Functions
from functions import feet_to_acres
#Variables 
feet = float(input('Square footage: '))
acres = feet_to_acres(feet) 
print(f'{acres} acres is equivalent to {feet:,.2f}')