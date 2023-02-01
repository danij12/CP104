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
def list_factors(num):
    """
    -------------------------------------------------------
    Takes an integer greater than 0 and finds its factors.
    Use: num_list = list_factors(num)
    -------------------------------------------------------
    Parameters:
       num_list - positive integer(int)
    Returns:
       num_list - A list of the factors
    -------------------------------------------------------
    """
    num_list = []
    count = 1
    while count != num:
        if num %count == 0:
            num_list.append(count)
        count+=1
    return num_list

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    num = int(input('Enter a positive number: '))
    positive_list = []
    while num!= 0:
        if num >0: 
            positive_list.append(num)
        num = int(input('Enter a positive number: '))
    return positive_list

def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    count = 0
    for a in values:
        if values[count] == target:
            locations.append(count)
        count+=1
    return locations
 

def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in subtrahend:
        while i in minuend:
            index = minuend.index(i)
            minuend.pop(index)

    return
 
 


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    i = 1
    while in_order and i <= len(values) - 1:
        if values[i] < values[i-1]:
            in_order = False
            index = i 
        i += 1
    return in_order, index
