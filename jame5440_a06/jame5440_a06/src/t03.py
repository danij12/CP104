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
from functions import interest_table

principal = float(input('Enter Principal Amount: '))
rate = float(input('Enter yearly interest rate: '))
payment = float(input('Enter monthly payment: '))

print(f'----------------------------------')
print(f'Month Interest   Payment   Balance')
print(f'----------------------------------')
interest_table(principal, rate, payment)
