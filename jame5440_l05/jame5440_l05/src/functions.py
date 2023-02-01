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
#Imports
import math
from pickle import TRUE, FALSE

def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    num1 = abs(target-v1)
    num2 = abs(target - v2)
    chosen_num = 0
    if num1 <= num2:
        chosen_num = v1
    else:
        chosen_num = v2
    return chosen_num


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    leap_year = False
    centurial = year - (year % 100)
    if year % 4 == 0 and year % 100 != 0 :
        leap_year = True
    elif year % 4 == 0 and year % 100 == 0 and centurial%400 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year


def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    result = ''
    if intensity < 5:
        result = 'Little or no damage'
    elif intensity >= 5 and intensity < 5.5:
        result = 'Some damage'
    elif intensity >= 5.5 and intensity < 6.5:
        result = 'Serious damage: walls may crack or fall'
    elif intensity >= 6.5 and intensity < 7.5:
        result = 'Disaster: buildings may collapse'
    elif intensity>= 7.5:
        result = 'Catastrophe: most buildings destroyed'
    else:
        result = 'Unknown'
    return result


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    MIN_YEARS = 5 
    MIN_SALARY = 30000
    qualified = False
    years = int(input('Years employed: '))
    if  years >= MIN_YEARS:
        salary = int(input('Annual salary: '))
        if salary >= MIN_SALARY:
            qualified = True 
        else:
            qualified = False
    else:
        qualified = False
    
    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    
    order = input('Order B -burger or W - wings: ')
    combo = input('Make it a combo? (Y/N): ')
    price = 0
    BURGER_PRICE = 6.00
    WINGS_PRICE = 8.00
    FRIES_PRICE = 1.50
    SALAD_PRICE = 2.00 
    if combo == 'Y':
        menu = input('Add F - fries or S - salad: ')
        if order == 'B' and menu == 'F':
            price = BURGER_PRICE + FRIES_PRICE
        elif order == 'B' and menu == 'S':
            price = BURGER_PRICE + SALAD_PRICE
        elif order =='W' and menu =='F':
            price = WINGS_PRICE + FRIES_PRICE
        elif order == 'W' and menu =='S':
            price = WINGS_PRICE + SALAD_PRICE
    elif combo == 'N':
        if order == 'B':
            price = BURGER_PRICE
        elif order == 'W':
            price = WINGS_PRICE
    return price
        