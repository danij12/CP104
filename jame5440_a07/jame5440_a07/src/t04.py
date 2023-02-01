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
from functions import subtract_lists,list_positives
minuend = list_positives()
print()
subtrahend = list_positives()

subtract_lists(minuend, subtrahend)
print(f'Minuend after: {minuend}')