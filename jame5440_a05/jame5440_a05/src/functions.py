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
from _tracemalloc import start

def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    ans = 1
    for n in range(1,num+1):
        ans *= n 
    return ans

def calories_burned(per_minute, minutes):
    """ calories_burned prints a table of the number of calories 
    burned every five minutes given 
    ------------------------------------------------------
    Use: burned = calories_burned(per_minute,minutes)
    ------------------------------------------------------
    Parameters: per_minute - calories burned per minute (float)
                minutes - total number of minutes (int)
    Returns: results of calories burnt every five minutes
        
    """
    burned = 0 
    for a in range(5,minutes+1,5):
        burned = per_minute *a
        print(f'{a}:   {burned:.1f}')
        
    return burned


def open_triangle(num_rows):
    """ open_triangle prints a character of  "#" with an empty centre
    Use: triangle =  open_triangle(num_rows)
      ------------------------------------------------------
      Parameters: num_rows- a number(int>0)
        ------------------------------------------------------
        Returns: 
    """
    space = 0
    for a in range(num_rows):
        print('#',end='')
        for b in range(a):
            print('',end=' ')
        print('#')
    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("       ", end="")
    for a in range(start, stop + 1):
        print(f"{a:5d}", end="")

    print()
    dashes = "-----" * (stop - start + 1)
    print(f"       {dashes}")

    for num1 in range(start, stop + 1):
        print(f"{num1:5d} |", end="")

        for num2 in range(start, stop + 1):
            product = num1 * num2
            print(f"{product:5d}", end="")

        print()

    return
    
    
def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    ans = 0 
    for a in range(count):
        ans+=start
        start+=increment
    return ans
      

