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
from functions import find_shortest
print("file 'words.txt' open for reading")
fh = open('words.txt','r')
word  = find_shortest(fh)
print(f"'{word}' is the first shortest word")