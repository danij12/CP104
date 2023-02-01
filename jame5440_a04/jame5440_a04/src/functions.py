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
def day_of_week(day_number):
    """  takes an integer parameter and returns a string representing the corresponding day of the week, 
         where 1 = "Monday", 2 = "Tuesday", up to 7 = "Sunday".
         The function returns "Error" if the parameter is a number outside the range of 1 through 7. 
         Assume that the parameter is an integer. 
         Use: day = day_of_week(day_number)
         -------------------------------------------------------
         Parameters: day_number- Integer number for day of the week
         (1<=int<=7)
         
         Returns: Day of the week
    """
    day = ''
    if day_number >= 1 and day_number<= 7:
        if day_number == 1:
            day = 'Monday'
        elif day_number == 2:
            day = 'Tuesday'
        elif day_number == 3:
            day = 'Wednesday'
        elif day_number == 4:
            day = 'Thursday'
        elif day_number == 5:
            day = 'Friday'
        elif day_number == 6:
            day_number = 'Saturday'
        elif day_number == 7:
            day = 'Sunday'
    else:
        day = 'Error'
    return day

def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    quality = ''
    
    if aqi >= 0 and aqi<= 50:
        quality = 'Good'
    elif aqi>= 51 and aqi<= 100:
        quality = 'Moderate'
    elif aqi>= 101 and aqi<=150:
        quality = 'Unhealthy for Sensitive Groups'
    elif aqi>=151 and aqi<=200:
        quality = 'Unhealthy' 
    elif aqi>=201 and aqi<=300:
        quality = 'Very Unhealthy'
    elif  aqi>= 300:
        quality = 'Hazardous'
    else:
        quality = 'Error'
    return quality
            
def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    bigger_num = 0
    if v1 > v3:
        if v2>v3:
            bigger_num = v1*v2
    elif v1> v2:
        if v3>v2:
            bigger_num = v1*v3
    elif v2 and v3 > v1:
        bigger_num = v2*v3

  
    return bigger_num

def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    colour = ''
    if (rgb1 == 'red' and rgb2 == 'blue') or (rgb2 == 'red' and rgb1 == 'blue'):
        colour = 'fuchsia'
    elif (rgb1 == 'red' and rgb2 == 'green') or (rgb2 == 'red' and rgb1 == 'green'):
        colour = 'yellow'
    elif rgb1 == 'green' and rgb2 == 'blue' or rgb2 == 'green' and rgb1 == 'blue':
        colour = 'aqua'
    elif rgb1 == 'red' and rgb2 == 'red':
        colour = 'red'
    elif rgb1 == 'blue' and rgb2 == 'blue':
        colour = 'blue'
    elif rgb1 == 'green' and rgb2 == 'green':
        colour = 'green'
    else:
        colour = 'Error'
    return colour


def yee_ha(number):
    """  yee_ha takes an integer parameter and returns one of the following strings:
        "Yee" if number is evenly divisible by 3
        "Ha" if number is evenly divisible by 7
        "Yee Ha" if number is evenly divisible by both 3 and 7
        "Nada" if number is none of the above
        Use:  response = yee_ha(number)
        -------------------------------------------------------
        Parameters: number - integer number (int)
        Returns: response - A response (str)
        """
    response = ''
    if number%3 == 0:
        response = 'Yee'
        if  number%7 == 0:
             response = 'Yee Ha'
    elif number%7 == 0 :
        response = 'Ha'
    else:
        response = 'Nada'
    return response
