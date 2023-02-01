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
from functions import date_extract

#Variables
num = int(input('Enter a date in the format MMDDYYYY: '))
date = date_extract(num)
print(f'The reformatted date: {date[0]}/{date[1]}/{date[2]}')