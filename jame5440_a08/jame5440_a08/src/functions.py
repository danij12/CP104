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
from pickle import TRUE, FALSE
def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    new_word = ''
    count = 0
    temp = 0 
    capital = 0 
    while count < len(string):
        if string[count].isupper() == True:
            if capital<2:
                if capital ==1:
                    new_word = new_word +string[temp:count]+ ' '
                capital +=1
                temp = count
            else:
                new_word = new_word + string[temp:count].lower() + ' '
                temp = count
        count+=1
    new_word = new_word + string[temp:len(string)].lower() + ' '
    new_word = new_word.strip()
    
    return new_word

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    plural = string

    if string.endswith(('s', 'sh', 'ch')):
        plural = plural + 'es'
    elif string.endswith('y') and not string.endswith(('ay', 'oy')):
        plural = plural.replace('y', 'ies')
    else:
        plural = plural + 's'
    return plural
            

def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    count = 1
    num = 0 
    common = 'none'
    
    while num == 0:
        if string1[len(string1)-count] == string2[len(string2)-count]:
            common = string1[len(string1)-count:len(string1)]
            count+=1
        else:
            num = 1
    
    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True 
    count = 0
    
    while count<len(isbn):
        if isbn[count] != '-' and isbn[count].isdigit() != True:
            valid = False 
        count+=1
        
    if len(isbn) != 17:
        valid = False 
    
    if isbn[len(isbn)-1].isdigit() == False and isbn[len(isbn)-2] != '-':
        valid = False 
    temp = isbn.split('-')
    for a in range(5):
        if temp[a].isdigit() == False:
            valid = False 
    if temp[0] != '978' and temp != '979':
        valid = False 
    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True 
    temp = ''
    temp2 = ''
    for a in range(len(word_list)-1):
        temp = word_list[a]
        temp2 = word_list[a+1]
        if temp[len(temp)-1] != temp2[0]:
            word_chain = False 
    
    return word_chain


            