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
from pickle import NONE, TRUE
def winner():
    """ 
    Determines Winner
    Use: won = winner()
    -------------------------------------------------------
    Parameters:
    None
    Returns:   
    Amount of times blue appeared in the input and how many time grey appeared
    """
    blue = 0
    grey = 0 
    win = None
    while win!='':
        win = input('Enter the winning team: ')
        if win == 'blue':
            blue+=1
        elif win == 'grey':
            grey+=1
    return blue,grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    i = 2
    while i < num and prime:
        if num % i == 0:
            prime = False
        else:
            i += 1
    
    return prime

def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f'Principal:     ${principal:.2f}')
    print(f'Interest Rate:     {rate:.1f}')
    print(f'Monthly Payment:    ${payment:.2f}')
    print(f'----------------------------------')
    print(f'Month Interest   Payment   Balance')
    print(f'----------------------------------')
    
     
    
    balance = principal
    month = 1
    
    while balance != 0:
        interest =balance*(rate/100/12)
        if payment>=balance:
            payment = balance + interest
            balance = 0.0
        else:
            balance = balance - payment+interest
        print(f"{month:5d}{interest:9.2f}{payment:10.2f}{balance:10.2f}")
    
        month += 1
        
    return

def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 1
    
    while num >= 10 or num <= -10:
        num /= 10
        count += 1
        
    return count
    
    
def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    x = num - 1
    total = 0
    while x > 0 :
        value = num % x 
        if value == 0 :
            total = total + x
            num = num/x
        x = x - 1
    return total