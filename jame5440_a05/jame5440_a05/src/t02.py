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
from functions import calories_burned
per_minute = float(input('How many calories are being burnt per-minute: '))
minutes = int(input('total number of minutes ran: '))
calories_burned(per_minute, minutes)
