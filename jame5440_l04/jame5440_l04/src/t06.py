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
from functions import pythag
#variables 
s1 = float(input('Length of side 1: '))
s2 = float(input('Length of side 2: '))
rad = pythag(s1,s2)
diameter = pythag(s1,s2)
circ = pythag(s1,s2)
area_circle = pythag(s1,s2)


print(f'Radius of resulting circle: {rad[0]}')
print(f'Diameter of resulting circle: {diameter[1]}')
print(f'Circumference of resulting circle: {circ[2]}')
print(f'Area of resulting circle: {area_circle[3]}')

