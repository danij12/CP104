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
from functions import get_addresses
fh = open('addresses.txt', 'r', encoding='utf-8')
addresses = get_addresses(fh)
fh.close()
for i in addresses:
    print(i)