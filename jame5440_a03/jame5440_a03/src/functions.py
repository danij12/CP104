"""
-------------------------------------------------------
Lab/Assignment  Testing
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
Version: 2021-10-18
-------------------------------------------------------
"""
#Functions
import math 
from random import randint
def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    conversion = 43560
    
    acres = round(square_footage/conversion,2)
    return acres


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    time = (width*length)/speed
    return time

def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    month = date_number // 1000000
    temp = date_number // 10000
    day = temp % 100
    year = date_number % 10000
    return(year,month,day)

def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    num  = num1 * num2
    denom = denom1 * denom2
    product =num/denom
    return num,denom,product

def math_quiz():
    """
    --------------------------------------------------------
    Adds two random numbers and asks the user for the answer.
    Then it prints the users answer as well as the expected answer
    ---------------------------------------------------------
    Documentation does not have 'Returns:'
    """
    num1 = randint(0,999)
    num2 = randint(0,999)
    print(f'  {num1:2}')
    print(f'+ { num2}')
    print('')
    ans = num1 + num2
    user_ans = int(input('Your answer: '))
    print('')
    print(f'Your answer: {user_ans:4}')
    print(f'Expected: {ans:7}')
    return 
    