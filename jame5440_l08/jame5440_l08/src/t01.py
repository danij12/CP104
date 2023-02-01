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
from functions import get_weekday_name
d = int(input('Enter a number that corresponds to a day of the week: '))
name = get_weekday_name(d)
print(name)