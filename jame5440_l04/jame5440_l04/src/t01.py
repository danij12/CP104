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
#1, 6, 9, 12, 14    
#Imports
from functions import diameter
#variables
radius = float(input('Enter radius: '))
diam = diameter(radius)
print(f'Diameter of circle: {diam}')