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
from functions import rgb_mix
rgb1 = input('Enter a colour: ')
rgb2 = input('Enter a second colour: ')
colour = rgb_mix(rgb1,rgb2)
print(f'rgb_mix("{rgb1}","{rgb2}") -> "{colour}"')
