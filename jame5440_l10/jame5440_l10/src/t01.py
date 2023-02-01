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
from functions import customer_record 
fh = open('customers.txt','r')
print('Find record n')
n = int(input('Enter a record number: '))
result = customer_record(fh,n)
print(f'{result}')
