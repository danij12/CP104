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
from functions import mow_lawn
#Variables
width = float(input('Width (m): '))
length = float(input('Length (m): '))
speed = float(input('Speed (m^2/minutes): '))
time = mow_lawn(width,length,speed)
print(f'Mowing the lawn takes {time:.0f} minutes' )