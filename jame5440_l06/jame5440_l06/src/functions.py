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
#1, 6, 10, 12, 15  
def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    sum = 0
    for i in range(2,num+1,2):
        sum +=i
    return sum

def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    num = 1
    for a in range(height):
        for b in range(height-1,a,-1):
            print(' ', end='')
        for c in range(0,num,1):
            print(f'{char}',end='')
        print()
        num +=2
    return  

def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    ans = 0
    count = inc
    for i in range(start,end+1,inc):
        ans += burnt_per_minute*inc
        print(f'Calories burned after {count} minutes: {ans}')
        count +=inc
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    n = 0
    intrest_value = 0
    temp = value
    final_value = value
    print(f'Year       Value $')
    print(f'------------------')
    for i in range(years+1):
        print(f'{i}           {temp:,}')
        intrest_value = temp*(rate/100)
        final_value +=intrest_value
        temp = round(final_value,2)
    
    return round(final_value,2)


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """ 
    value = float(input('First value: '))
    total = value 
    minimum = value 
    maximum = value 
    
    for i in range(n-1):
        new_value = float(input('Next value: '))
        total += new_value
        
        if new_value > maximum:
            maximum = new_value
        elif new_value < minimum:
            minimum = new_value
    average = total/n
    return minimum,maximum,total,average
        