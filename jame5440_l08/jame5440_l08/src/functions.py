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
#1, 4, 7, 13, 15    
from random import randint
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    list1 = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    return list1[d-1]

def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    num = 0
    list1 = []
    while num!= n:
        list1.append(randint(low,high))
        num+=1
    return list1


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negative = 0
    positive = 0  
    zeroe = 0 
    even = 0 
    odd = 0 
    for a in values:
        if a<0:
            negative +=1
        elif a == 0:
            zeroe +=1
        else:
            positive +=1
        if a%2 == 0:
            even +=1
        else:
            odd += 1
    return negative,positive,zeroe,even,odd

def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    list1 = source1 + source2
    final_list = []
    for a in list1:
        if a not in final_list:
            final_list.append(a)
    return final_list


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    list1 = source1 + source2
    final_list = []
    for b in list1:
        if b in source1:
            if b in source2:
                list1.remove(b)
        elif b in source2:
            if b in source1:
                list1.remove(b)
    for a in list1:
        if a not in final_list:
            final_list.append(a)
    for b in final_list:
        if b in source1:
            if b in source2:
                final_list.remove(b)
        elif b in source2:
            if b in source1:
                final_list.remove(b)
    return final_list
            