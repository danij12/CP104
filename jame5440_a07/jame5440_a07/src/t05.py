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
from functions import is_sorted, list_positives

values = list_positives()
in_order, index = is_sorted(values)
print(f"True or False: {in_order}")
print(f"Index: {index}")