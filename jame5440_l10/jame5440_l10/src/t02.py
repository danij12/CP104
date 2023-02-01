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
from functions import customer_by_id
fh = open('customers.txt','r')
print('Find customer by id_number')
id_number = input('Enter an ID: ')
person = customer_by_id(fh, id_number)
print(f'{person}')

