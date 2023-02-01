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
from random import randint

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 0
    number = randint(1,high)
    guess = 0
    
    while guess!= number:
        guess = int(input('Guess: '))
        if guess>number:
            print('Too high, try again.')
            count += 1
        elif guess<number:
            print('Too low, try again.')
            count += 1
        else:
            print('Congratulations-good guess!') 
            count+=1
    return count

def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    rate /=100
    years = 0
    while target>current:
        years+=1
        current +=(current*rate)
    return years

    
    

def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    num1 = float(input('First positive value: '))
    num2 = 0
    count = 1
    avg = num1
    total =  num1
    min = num1
    max = num1
    while num2 >=0: 
        if num2>=0:
             num2 = float(input('Next positive value: '))
             if num2>=0:
                 total += num2
                 count+=1
                 avg = total/count
                 print(count)
        if max<num2:
                max = num2
        if min >num2 and num2>=0:
                min = num2
            
    print(f'minimum: {min}')
    print(f'maximum: {max}')
    print(f'total: {total}')
    print(f'average: {avg}')
    return  min,max,total,avg

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    another_day = 'Y'
    day = 1
    b_total = 0 
    l_total = 0
    s_total = 0 
    grand_total = 0 
    while another_day == 'Y':
        breakfast = float(input('How much was breakfast? $'))
        lunch = float(input('How much was lunch? $'))
        supper = float(input('How much was supper? $'))
        total = breakfast+lunch+supper
        day+=1
        b_total +=breakfast
        l_total += lunch 
        s_total += supper
        print(f'Your total for the day was ${total}')
        print()
        another_day = input('Where you away another day (Y/N)? ')
        print()
        print(f'For Day {day}')
        print()
    grand_total = b_total+l_total+s_total
    print(f'Total: ')
    print(f'Breakfast:    $ {b_total:^2}')
    print(f'Lunch:        $ {l_total:^5}')
    print(f'Supper:       $ {s_total:^5.2f}')
    print()
    print(f'Grand total: ${grand_total}')
    return b_total,l_total,s_total,grand_total
    
            
def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    guess = 0
    while guess<=low or guess>high:
        guess = int(input(f'Enter a value between {low} and high {high}: '))
        if guess>high:
            print(f'Value entered is too high')
        elif guess<=low:
            print(f'Value entered is too low')
    return guess
                

