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
from functions import treadmill
burnt_per_minute = float(input('Enter calories burned per minute: '))
start = int(input('Enter beginning number of minutes: '))
end = int(input('Enter ending number of minutes: '))
inc = int(input('Enter the increment in minutes: '))

treadmill(burnt_per_minute,start,end,inc)


