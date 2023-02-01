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
from functions import is_word_chain

word_list = []
word = ""
while word != "0":
    word = str(input("Enter a word (input 0 to end): "))
    if word != "0":
        word_list.append(word)
    else:
        print(word_list)


word_chain = is_word_chain(word_list)


print(f"is_word_chain -> {word_chain}")