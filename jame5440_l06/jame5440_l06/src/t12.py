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
from functions import gic
value = int(input('Enter the GIC purchase value: '))
years = int(input('Enter the number of years invested: '))
rate = float(input('Enter the GIC intrest rate (%): '))
gic(value,years,rate)

